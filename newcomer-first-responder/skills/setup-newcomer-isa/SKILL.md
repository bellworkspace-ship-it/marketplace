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
Confirm these are in place before onboarding agents. The agent inherits all of it:
1. **Register the system** at https://apps.followupboss.com/system-registration to
   get the `X-System` / `X-System-Key` (raises rate limits and is required). This
   is baked into the plugin config — not per agent.
2. **Enable the API Key Restrictions power-up** so the owner can grant/revoke each
   agent's API access centrally (kill switch).
3. **Create owner-level webhooks** (e.g. `peopleCreated`, `peopleStageUpdated`) for
   near-real-time detection — only the Owner can do this.
4. **Create the shared team learning log** (a shared Google Sheet/Drive file) and
   share it with the team.
5. **Set brokerage defaults** (service-area zip lists, voice norms) — optional; the
   value/objection/cadence playbooks ship inside the plugin already.
6. **Publish the plugin** to the private Newcomer marketplace so agents install in
   two clicks.

## Agent setup (about 2 minutes)
1. **Install** the Newcomer plugins from the marketplace.
2. **Connect Follow Up Boss** — one-click **OAuth**: the agent signs in and
   consents as themselves. This scopes the ISA to *their own assigned leads only*
   (Agent role) — never broker-wide. (Fallback if needed: paste their key from
   FUB **Admin → API**.)
3. **Connect Google Calendar + Gmail** — one click each (for booking and email).
4. **Confirm the browser for sending** — make sure Chrome (or Edge) has FUB open
   and logged in; this is what actually sends texts, since the API can only log
   them. Confirm they can log into `https://coaching.revii.app` for referrals.
   If either logs out later, the ISA pings them and they reply "log me in"
   (see the ISA's login-dispatch behavior). Logins stay only on their device.
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
