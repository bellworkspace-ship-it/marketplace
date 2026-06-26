---
name: setup-newcomer-isa
description: >
  This skill should be used the first time an agent sets up the Newcomer First
  Responder ISA, or when they want to change its settings. It connects Follow Up
  Boss (one-click OAuth) and the agent's calendar/email, confirms the browser for
  sending texts and Revii, captures a few personalization details, and schedules
  the automatic run. Most configuration is pre-done by the broker so the agent
  does almost nothing. Triggers on "set up the ISA", "set up my first responder",
  "configure the Newcomer ISA", "onboard me", or "change my ISA settings".
metadata:
  version: "0.2.0"
  author: "The Newcomer Group"
---

# Set up the Newcomer First Responder ISA

The goal is near-zero effort for the agent. The broker has already done the heavy
configuration; the agent just connects their accounts and confirms a few
preferences. Keep all conversation plain-language and non-technical. Save the
agent's choices to a local settings note the ISA reads each run (`isa-settings.md`
in the agent's working folder — never in any shared repo).

## Broker setup (one time — done by Steven, not the agent)
**Beacon runs browser-first — no FUB API keys, no system registration, no webhooks
required.** The only must-dos:
1. **Create the shared team learning log** (a shared Google Sheet/Drive file) and
   share it with the team.
2. **Set brokerage defaults** (service area is preloaded to NE Florida; tweak voice
   norms if you want) — the value/objection/cadence playbooks ship in the plugin.
3. **Publish the plugin** to the Newcomer marketplace so agents install in two clicks.

> **Optional, advanced — headless API path (NOT needed to start).** If you ever want
> Beacon to read/log through the FUB *API* instead of the browser, that requires
> broker plumbing: register a system at apps.followupboss.com/system-registration,
> grant each agent **API access** via **Admin → Teams → "API Access" checkbox**
> (that's the *API Key Restrictions* power-up that showed your agent the "contact
> your account owner" message), add owner webhooks, and wire a FUB MCP. Until then,
> agents need **none** of this — just a logged-in FUB browser tab.

## Agent setup (about 2 minutes)
1. **Install** the Newcomer plugins from the marketplace.
2. **Connect Follow Up Boss — two quick parts:**
   - **API key (for efficient reading):** paste the agent's FUB API key once (FUB →
     **Admin → API**). Save it locally to **`~/.beacon/fub_key`** — that's what the
     Beacon Follow Up Boss connector uses to pull the work list and full lead context
     cheaply (the credit-efficient path). The key is scoped to the agent's **own
     leads** and stays on their device. *(If FUB shows "contact your account owner,"
     the Owner enables it via **Admin → Teams → API Access**. If you skip the key,
     Beacon falls back to reading in the browser — works, just costs more credits.)*
   - **Browser logged in (for sending):** keep FUB **open and logged in** in Chrome —
     that's how Beacon actually sends the texts (the API only logs them).
3. **Connect Google Calendar + Gmail** — one click each (for booking and email).
4. **Confirm Revii** — make sure the agent can log into
   `https://coaching.revii.app` for out-of-area referrals. If FUB or Revii logs out
   later, Beacon pings them and they reply "log me in" (login-dispatch). Tip: keep
   FUB "remembered"/logged in so it's always ready. Logins stay only on their device.
5. **Quick personalization** (pre-fill from broker defaults where possible):
   - **service area: preloaded to all of Northeast Florida** (`service-area-ne-florida.md`)
     — the agent enters **no zip codes**; only ask if they serve a *subset* and want
     to narrow it (e.g., St. Johns County only),
   - working/quiet hours (when it may send),
   - voice & signature (a couple of real text examples help),
   - alert channel for on-the-go pings (text to self / email / notification).
6. **Auto-schedule (one engine)** — schedule the **Smart List Manager** as the
   single recurring run on the agent's own Claude (their credits), e.g. **3× per day**
   (~9am, 1pm, 5pm), with the new-lead/handraiser lists checked **more often** (every
   ~15 min in working hours) for speed-to-lead. One engine = leads are never
   double-worked. (Browser sending needs their computer on and Claude running; true
   overnight coverage is the optional phase-2 texting provider.)
7. **Smart Lists, pace & opt-out controls** (responsible/controllable):
   - Review the agent's live smart lists and confirm which are **automated** vs
     **protected**. Defaults to protect: **Current Clients, Under Contract, Past
     Clients, Birthday, Closing Anniversary** (+ any the agent adds).
   - Set the **balanced pace** and per-list daily **caps** (see `smart-list-playbook.md`);
     remember each agent works only **their own** assigned leads/pond, so lists are
     small and usually clear daily.
   - Confirm the **Fishing Pond** for opt-outs (Do Not Contact tag + number/email
     marked + moved there).
   - Confirm **HomeLight** and **Fello** are recognized as sources.
8. **Booking rules** (so it can set appointments hands-off): appointment **types and
   durations** (e.g., 15-min call, 30-min buyer consult, 60-min valuation/listing,
   showing), appointment **hours**, buffers/travel time, max per day, and minimum lead
   time. The ISA conflict-checks the calendar and sends the lead an invite.
9. **MLS / valuation tools** (asked once, remembered forever): which tools the agent
   personally has — **Paragon, RPR/narrpr, Matrix, Stellar, Zillow, or other**. The
   ISA uses these (their own logins, in the browser) to answer listing/value
   questions and pull real comps; it reuses `newcomer-cma` if installed.
10. **Autonomy & alerts:** choose **Approve mode** (ISA drafts, agent one-taps) or
    **Auto mode** (ISA sends within guardrails) — new agents should start in Approve.
    Confirm what pings them immediately (hot reply, booked, escalation, "call me now")
    vs. what waits for the summary.

## Smart Lists (optional convenience)
The ISA can find leads directly via the API, but offer to create FUB Smart Lists
that make runs fast and human-reviewable: **New/unworked**, **Newly assigned to
me**, **Fello inquiries** (by Lead Score), **Follow-ups due today**.

## Finish
Summarize the agent's settings in plain language, confirm, and offer a **dry run**:
the ISA finds new leads and **drafts** (does not send) the first few messages so
the agent approves the voice before going live.
