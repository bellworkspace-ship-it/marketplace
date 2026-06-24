# Error handling & resilience (self-sustaining)

The ISA should heal itself silently and only bother the agent when truly blocked.
Follow these rules on every API interaction so agents never see integration errors.

## Respect rate limits (don't trip them in the first place)
FUB uses a **sliding 10-second window**, per context. Every response includes:
`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Window`, `X-RateLimit-Context`.

Current limits **with** the `X-System-Key` header (always send it):

| Context | Limit / 10s | Applies to |
|---|---|---|
| global | 250 | all requests |
| events (GET) | 20 | `GET /events` |
| PUT.people | 25 | `PUT /people` |
| notes | 10 | `/notes` |
| POST.events | unlimited* | `POST /events` |

Without `X-System-Key`, global drops to 125 and events GET to 10 — so always
register and send the system header.

**Budgeting rules:**
- Read `X-RateLimit-Remaining`; when it gets low for a context, slow down / batch.
- Work in small batches with brief pauses rather than firing hundreds of calls.
- For big jobs, periodically check `GET /rateLimit/usage` (24h rolling) and
  `GET /rateLimit/limits`.
- Prefer one efficient list call + targeted detail calls over scanning everything.

## Handle every status code correctly
- **200 / 201 / 204** — success.
- **400 Bad Request** — the body is JSON with an `errorMessage`. **Read it**, fix
  the parameters, and retry once. Do not blindly resend.
- **403 Forbidden** — either (a) the agent lacks access to that resource (skip it,
  it's out of their scope — expected), or (b) the **account is expired/locked
  down**. If many 403s appear, the account is likely expired: note that
  `POST /events` still works, pause other writes, and alert the agent/broker.
- **404 Not Found** — the record was deleted; skip and move on.
- **429 Too Many Requests** — you were throttled. **Wait the number of seconds in
  the `Retry-After` header, then retry.** Respect 429 even if `Remaining` looked
  positive. Never hammer.
- **5xx (500/503/504)** — server-side. Retry with **truncated exponential backoff
  + jitter**: wait ~1s, then ~2s, ~4s, ~8s… (each plus a random <1s), capped at
  32–64s, up to a sane max number of retries. Then stop and report.

## Don't create duplicates / don't lose data
- Before creating a person, call `GET /people/checkDuplicate`.
- Use `POST /events` (the preferred lead-intake path) so FUB de-dupes and routes
  correctly; it's unlimited and survives grace-period accounts.
- Logging a text/note that fails should be retried (backoff), never dropped — FUB
  is the system of record.

## Browser-session failures (the send step & Revii)
The API can't send texts, so sending uses the browser. If FUB or Revii is logged
out, don't fail silently — follow `session-and-login-dispatch.md`: alert the agent
on the go and offer the "log me in" dispatch, then rerun the blocked step.

## When to alert vs. self-heal
- **Self-heal silently:** transient 429/5xx, pagination, a single skipped 403/404,
  rate-limit pacing. The agent never needs to know.
- **Alert the agent:** logged-out browser session, expired FUB account, repeated
  hard failures, or anything that stops their leads from being worked. Make the
  alert plain-language and actionable ("reply 'log me in'", "your FUB account
  looks expired — here's what to do").

## Golden rules
1. Always send `X-System` / `X-System-Key`.
2. Watch the rate-limit headers; pace yourself.
3. Back off on 429/5xx; never spam retries.
4. Never drop a log/note — FUB must stay accurate.
5. Bother the agent only when they truly need to act.
