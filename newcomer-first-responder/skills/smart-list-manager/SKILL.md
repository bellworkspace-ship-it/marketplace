---
name: smart-list-manager
description: >
  This skill is the master engine that works the agent's entire Follow Up Boss
  pipeline by smart list — on a schedule — clearing the automated lists by moving
  leads forward, while leaving protected lists untouched. It covers new-lead speed,
  conversation follow-up, and long-term nurture in one coordinated run (so leads are
  never double-messaged), sets appointments, and handles replies and opt-outs.
  Triggers on "manage my lists", "work my smart lists", "clear my lists", "work my
  pipeline", "work my follow up boss lists", or its scheduled run.
metadata:
  version: "0.1.0"
  author: "The Newcomer Group"
---

# Smart List Manager (the pipeline engine)

Work the whole Follow Up Boss pipeline like an expert agent: go list by list,
follow up to each list's cadence, set appointments, and **clear the automated lists
by advancing leads to the next stage** — while never touching the protected lists.
This is the plugin's single scheduled engine: it includes the First Responder's
fast new-lead behavior, so there is no separate first-responder run and leads are
never worked twice.

**Connection & cost (read cheap, send via browser).** Prefer the **FUB API** for all
*reading* — the work list and each lead's full context — whenever a FUB connection is
configured; structured JSON is the cheapest, cleanest way to pull the database and
reaches the most leads per credit. Use the **browser only to send texts** (and Revii)
— that's the expensive part, so never browse to *read* when the API can. If no API
connection is set up yet, read FUB in the browser as **text** (`get_page_text`, never
screenshots) with strict caps. Spend the fewest tokens for the most quality touches —
follow `references/credit-efficiency.md` every run. Never block on the agent creating
an API key (some accounts restrict them).

## Operating principles
1. **Clear by advancing.** A lead leaves a list when you move them forward (reply →
   Spoke With; booked → Appointment Set; opted out → DNC/Pond). Working the lead is
   what clears the list.
2. **Balanced volume.** Respect per-list daily caps and quiet hours; prioritize
   newest, highest-intent, and most-overdue first. Don't blast big lists.
3. **One conversation.** Never message a lead twice in a run; coordinate across
   lists (`routing-and-dedup.md`). A live thread is handled once.
4. **Value every time, never "just checking in."**
5. **Opt-outs are absolute** (`opt-out-and-compliance.md`).
6. **Protected lists are off-limits** — never auto-contact them.
7. **Continue, don't restart** — pick up each lead's cadence where it left off.

## The run (on schedule)

### 1. Session & setup
Confirm FUB is **open and logged in** in the browser (login dispatch if needed) —
this is the connection, no API key. Load from setup: the **protected list set**,
**per-list caps**, the **balanced pace**, quiet hours, voice, MLS/valuation tools,
and autonomy mode.

### 2. Read the live smart lists
Call `GET /smartLists` to get the agent's actual lists and counts. Map each to the
**`smart-list-playbook.md`** (goal, cadence, exit condition). Split into **automated**
vs **protected** per setup. Skip protected lists entirely.

### 3. Build one global work queue (priority order, with caps)
Across the automated lists, in this order, applying each list's daily cap:
1. **New Lead** + **Digital-Handraisers** — fast, high-intent (First Responder speed).
2. **Appointment Set** — confirmations/reminders; **no-shows → re-engage** (`bailed-appointment-reengagement.md`).
3. **Met With Customer** — advance, or **re-engage if ghosted** (`bailed-appointment-reengagement.md`).
4. **Spoke With Customer** — drive to appointment.
5. **Attempted Contact** — earn a first reply.
6. **Nurture Now! → 3–12 Months → Long Term** — value touches, strict caps (esp. Long Term).
Always honor dedup/cooldown so a lead in two lists is worked once.

### 4. Work each lead (per-lead engine)
For each queued lead: read full context (and *why* they're on this list), then apply
the shared per-lead engine — read intent (`lead-context-and-fello.md`,
`homelight.md`), compose value-first (`value-message-library.md`,
`message-style-guide.md`), answer real questions (`mls-and-valuation-data.md`),
handle replies/objections (`objection-playbook.md`), and book
(`scheduling-and-booking.md`) — framed to that list's goal and cadence.

### 5. Replies, opt-outs, escalations first
- Opt-out → full flow (`opt-out-and-compliance.md`) and stop.
- Objection/question → handle and add value.
- Sensitive/complex/VIP/"call me" → escalate with a brief (`escalation-alerts-autonomy.md`).

### 6. Advance the stage to clear the list
After acting, update the stage (`stage-workflow.md`) so the lead drops off the list:
replied → Spoke With; booked → Appointment Set; met → next step; exhausted → Nurture;
opted out → Trash + Fishing Pond. **Updating the stage is what clears the list.**

### 7. Log & report
Append anonymized outcomes (`learning-log.md`). End with a **per-list summary**:
for each automated list — worked, advanced/cleared, appointments set, opt-outs, and
anything held for the agent.

## Protected lists (never auto-contact)
By default: **Current Clients, Under Contract, Past Clients, Birthday, Closing
Anniversary** (plus any others the agent marks protected in setup). Leave these
entirely alone.

## References
- `references/credit-efficiency.md` — fewest credits for the most quality touches (read every run)
- `references/smart-list-playbook.md` — per-list goals, cadences, caps, exit conditions
- `references/bailed-appointment-reengagement.md` — Appointment Set no-shows & Met-With-Customer ghosting
- `references/stage-workflow.md` · `references/cadence-rules.md` · `references/routing-and-dedup.md`
- `references/value-message-library.md` · `references/message-style-guide.md` · `references/objection-playbook.md`
- `references/scheduling-and-booking.md` · `references/mls-and-valuation-data.md` · `references/escalation-alerts-autonomy.md`
- `references/opt-out-and-compliance.md` · `references/lead-context-and-fello.md` · `references/homelight.md`
- `references/fub-api-reference.md` · `references/error-handling-and-resilience.md` · `references/session-and-login-dispatch.md` · `references/learning-log.md`
