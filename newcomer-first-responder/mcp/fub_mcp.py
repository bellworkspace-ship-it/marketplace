#!/usr/bin/env python3
"""
Beacon — Follow Up Boss connector (MCP).

Credit-efficient read/write access to Follow Up Boss using the AGENT'S OWN API key,
so Beacon can pull the work list and read full lead context cheaply (structured JSON),
instead of browsing the FUB web UI.

Run locally:  FUB_API_KEY=your_key python3 fub_mcp.py
Dependency:   pip install fastmcp     (HTTP uses the Python standard library)

Scope: an Agent-role key only sees that agent's assigned leads — never broker-wide.
The key is read from the environment and is never logged or stored by this server.
"""
import os, json, base64, time
import urllib.request, urllib.parse, urllib.error
from fastmcp import FastMCP

API = "https://api.followupboss.com/v1"
XSYS = os.environ.get("FUB_X_SYSTEM", "Beacon").strip()
XKEY = os.environ.get("FUB_X_SYSTEM_KEY", "").strip()

mcp = FastMCP("beacon-fub")


def _load_key():
    """Find the agent's FUB API key: env var first, then a local file Beacon's setup writes."""
    k = os.environ.get("FUB_API_KEY", "").strip()
    if k:
        return k
    for p in (os.path.expanduser("~/.beacon/fub_key"),
              os.path.join(os.path.dirname(os.path.abspath(__file__)), "fub_key.txt")):
        try:
            with open(p) as fh:
                v = fh.read().strip()
                if v:
                    return v
        except Exception:
            pass
    return ""


def _headers():
    key = _load_key()
    if not key:
        raise RuntimeError("No Follow Up Boss API key found. Run Beacon's setup to save your "
                           "key (it writes ~/.beacon/fub_key), or set the FUB_API_KEY env var.")
    h = {
        "Authorization": "Basic " + base64.b64encode((key + ":").encode()).decode(),
        "Content-Type": "application/json",
    }
    if XKEY:
        h["X-System"] = XSYS
        h["X-System-Key"] = XKEY
    return h


def _req(method, path, params=None, body=None, _retry=0):
    url = API + path
    if params:
        clean = {k: v for k, v in params.items() if v not in (None, "")}
        if clean:
            url += "?" + urllib.parse.urlencode(clean)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            txt = resp.read().decode()
            return json.loads(txt) if txt else {}
    except urllib.error.HTTPError as e:
        code = e.code
        raw = e.read().decode(errors="ignore")
        if code == 429 and _retry < 4:
            time.sleep(int(e.headers.get("Retry-After", "5")))
            return _req(method, path, params, body, _retry + 1)
        if code >= 500 and _retry < 3:
            time.sleep(2 ** _retry)
            return _req(method, path, params, body, _retry + 1)
        if code == 403:
            raise RuntimeError("403 Forbidden — this FUB key lacks API access. Ask the "
                               "account owner to enable it (Admin → Teams → API Access), "
                               "or the account may be expired.")
        msg = raw[:300]
        try:
            msg = json.loads(raw).get("errorMessage", msg)
        except Exception:
            pass
        raise RuntimeError(f"FUB {method} {path} → {code}: {msg}")


# ---------------------------------------------------------------- read (cheap) --
@mcp.tool()
def whoami() -> dict:
    """Confirm the API key works and show the authenticated FUB user (their scope)."""
    return _req("GET", "/me")


@mcp.tool()
def list_smart_lists() -> list:
    """List the agent's FUB smart lists (id, name, count) so Beacon knows which to work."""
    d = _req("GET", "/smartLists")
    lists = d.get("smartlists") or d.get("smartLists") or []
    return [{"id": s.get("id"), "name": s.get("name"), "count": s.get("count")} for s in lists]


@mcp.tool()
def get_work_list(stage: str = "", limit: int = 50, offset: int = 0) -> list:
    """Pull a COMPACT work list in ONE call — the cheap way to see who to work this run.
    Optionally filter by stage name (e.g. 'Attempted Contact'). Returns id, name, stage,
    source, last activity, tags, and whether a mobile/email exists. Use this to build the
    queue and triage; do NOT call get_person until you've decided to work a lead."""
    params = {"limit": min(max(limit, 1), 100), "offset": offset, "sort": "updated"}
    if stage:
        params["stage"] = stage
    d = _req("GET", "/people", params=params)
    out = []
    for p in d.get("people", []):
        phones = p.get("phones") or []
        out.append({
            "id": p.get("id"),
            "name": p.get("name") or f"{p.get('firstName','')} {p.get('lastName','')}".strip(),
            "stage": p.get("stage"),
            "source": p.get("source"),
            "lastActivity": p.get("lastActivity") or p.get("updated"),
            "hasMobile": any((ph.get("value") for ph in phones)),
            "hasEmail": bool(p.get("emails")),
            "tags": p.get("tags", []),
        })
    return out


@mcp.tool()
def get_person(person_id: int) -> dict:
    """Full context for ONE lead — call only for leads you'll actually work. Returns stage,
    tags, source, all custom/Fello fields, and the 10 most recent notes. This is what Beacon
    reads to decide the right re-approach or whether to set the appointment."""
    p = _req("GET", f"/people/{person_id}", params={"fields": "allFields"})
    try:
        notes = _req("GET", "/notes",
                     params={"personId": person_id, "limit": 10, "sort": "-created"}).get("notes", [])
    except Exception:
        notes = []
    p["_recentNotes"] = [{"created": n.get("created"), "body": (n.get("body") or "")[:600]} for n in notes]
    return p


@mcp.tool()
def list_stages() -> list:
    """List the account's stages (id + name) so Beacon maps to the real, standard stage set."""
    return [{"id": s.get("id"), "name": s.get("name")} for s in _req("GET", "/stages").get("stages", [])]


# --------------------------------------------------------------- write (log) ---
@mcp.tool()
def add_note(person_id: int, note: str) -> dict:
    """Log a note on a lead (what Beacon did/said), keeping FUB the system of record."""
    return _req("POST", "/notes", body={"personId": person_id, "body": note})


@mcp.tool()
def set_stage(person_id: int, stage: str) -> dict:
    """Advance a lead's stage by name (e.g. 'Spoke With Customer', 'Appointment Set').
    Moving the stage is what clears a smart list."""
    return _req("PUT", f"/people/{person_id}", body={"stage": stage})


@mcp.tool()
def create_task(person_id: int, description: str, due_date: str = "") -> dict:
    """Create a follow-up task on a lead (the next touch). due_date is optional ISO YYYY-MM-DD."""
    body = {"personId": person_id, "name": description}
    if due_date:
        body["dueDate"] = due_date
    return _req("POST", "/tasks", body=body)


@mcp.tool()
def create_appointment(person_id: int, title: str, start: str, end: str,
                       location: str = "", description: str = "") -> dict:
    """Book an appointment in FUB after confirming the time on the agent's calendar.
    start/end are ISO datetimes (e.g. 2026-06-26T15:00:00-04:00)."""
    body = {"title": title, "start": start, "end": end, "invitees": [{"personId": person_id}]}
    if location:
        body["location"] = location
    if description:
        body["description"] = description
    return _req("POST", "/appointments", body=body)


@mcp.tool()
def rate_limit_usage() -> dict:
    """Check remaining FUB API budget (so Beacon can pace itself and avoid 429s)."""
    return _req("GET", "/rateLimit/usage")


if __name__ == "__main__":
    mcp.run()
