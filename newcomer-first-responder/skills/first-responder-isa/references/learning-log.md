# Team learning log (anonymized, shared)

How the ISA gets smarter for the whole team over time. This is not model
training — it's a shared record of what's working that the ISA reads before
composing and appends to after acting.

## Where it lives
A single shared store the whole team can read/write — a shared Google Sheet (or
Drive file) created during setup. Setup stores its location. Every agent's ISA
uses the same shared log so wins compound across Newcomer.

## Read before composing
At the start of message composition, read recent entries and bias toward:
- the **value types** with the highest reply/appointment rates right now,
- the **send-time windows** that are getting replies,
- the **objection rebuttals** that are converting,
- patterns for the **lead type** at hand (buyer / seller / Fello / referral).

## Append after acting
After each meaningful action, append one row. Keep it **anonymized** — outcomes
and categories only, never lead PII.

| Field | Example values |
|---|---|
| date | 2026-06-23 |
| time_bucket | morning / afternoon / evening / weekend |
| lead_type | buyer / seller / fello_value / investor / sphere / referral |
| lead_temp | new / hot / warm / cold |
| value_type | listing / value_update / market_stat / answer / resource |
| objection_type | none / has_agent / not_ready / price / commission / other |
| action | text / email / referral / appointment |
| result | reply / no_reply / appointment / opt_out / referral_made |

## Privacy rules (hard)
- **No PII** ever in the log — no names, numbers, emails, or addresses.
- No agent identity beyond an optional anonymized id; default to none for a pure
  team aggregate.
- The log captures *what kind of message worked when*, not *who* it was sent to.

## How it improves results
Over weeks, the log reveals the team's real playbook: which value angles open
which lead types, the best times to reach people, and the rebuttals that turn
objections into appointments. The ISA leans into those, so every agent benefits
from the whole team's experience — a genuine, compounding edge.
