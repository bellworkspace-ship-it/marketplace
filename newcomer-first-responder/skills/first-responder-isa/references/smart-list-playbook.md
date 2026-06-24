# Smart List playbook (per-list goals, cadence, caps, exit)

How to work each Follow Up Boss smart list and how it clears. Read the live lists
with `GET /smartLists` and map by meaning — names/counts vary by agent.

## Scope: each agent works only their own
Every agent's ISA operates on **their own assigned leads and their own pond**
(Agent-role access), so their lists are much smaller than the broker's aggregate
admin view. Caps below are **per agent** and scale to their volume — for most agents
the lists are small enough to keep fully cleared day to day.

## Automated lists (worked + cleared)

| List | Goal | Cadence | Suggested daily cap* | Clears when |
|---|---|---|---|---|
| **New Lead** | Instant speed-to-lead | Respond in minutes; daily wk 1 | all (usually few) | reply → Spoke With |
| **Digital-Handraisers** | Catch intent, identify need, book | Fast on entry, 1/day ×5, taper | all–25 | reply / book |
| **Appointment Set** | Make sure they show | Confirm + reminder day-before & morning-of; no-show → re-engage | all | attended → Met With / rebooked |
| **Met With Customer** | Advance to client, or re-set if ghosted | 24–48h post-meeting, then every 2–3 days | all | becomes client / → Nurture |
| **Spoke With Customer** | Book the appointment | Every 2–3 days, tighten if engaged | ~25–40 | booked → Appointment Set |
| **Attempted Contact** | Earn a first reply | Vary channel/time, 1/day ×7–10, then every 2–3 days to day 21 | ~25–40 | reply → Spoke With / exhausted → Nurture |
| **Nurture Now!** | Stay top-of-mind, catch signals | 1 strong value touch/week | ~20–30 | re-engages → forward |
| **Nurture 3–12 Months** | Mid-term warm-up | Every 2–4 weeks (market/value/equity) | ~20–30 | heats up → forward |
| **Nurture Long Term** | Slow reactivation | ~Monthly, oldest/highest-intent first | ~15–25 | re-engages → forward |

*Caps are starting points for the **balanced** pace; tune in setup. They protect
deliverability and compliance. Always prioritize newest, highest-intent, most-overdue.

## Protected lists (never auto-contact)
Default: **Current Clients · Under Contract · Past Clients · Birthday · Closing
Anniversary** (+ any others the agent marks protected). Skip entirely.

## Clearing = advancing the stage
A lead leaves a list when you move them to the next stage (`stage-workflow.md`).
Work the lead → they reply/book/opt-out → they drop off. New entries get worked the
next run, so lists stay current.

## List hygiene for clean automation
Lists anchored to a **stage** ("Stage = Attempted Contact") clear permanently when
the stage advances. Lists based only on "no activity in N days" will re-add people —
fine for nurture, but flag them so the agent knows they recycle. Offer to help anchor
the key automated lists to stages.
