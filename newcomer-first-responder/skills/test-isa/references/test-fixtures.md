# Test fixtures (sample leads)

Synthetic leads for simulation mode. Each mimics how a lead really lands in FUB,
including Fello's note-based detail. Use these to run the ISA and self-grade.
No real people; safe to use anytime.

---

## Fixture 1 — Fello home-value, LOCAL (St. Augustine)
- **Person:** Karen M. · recently assigned · source: Fello
- **Note (Fello):** "Home Value request — 142 Sandpiper Ln, St. Augustine FL 32084.
  Viewed valuation dashboard 2x this week."
- **Fello fields:** Est. value $absent, Lead Score: High, Equity: high.
- **Expected:** detect Fello home-value (local) → local seller/value play → message
  references the St. Augustine address + one value angle → asks for a short callback
  → FUB note + stage to Engaged + follow-up task. **No referral.**

## Fixture 2 — Fello home-value, OUT-OF-STATE address + St. Augustine history (RELOCATION BUYER)
- **Person:** Dave R. · recently assigned · source: Fello
- **Note (Fello):** "Home Value request — 88 Birch St, Columbus OH 43215."
- **History:** prior buyer inquiry 8 months ago searching St. Augustine 32092 homes
  $450–550k; opened 3 listing emails.
- **Expected:** detect intent = **relocation buyer** → **work locally, do NOT
  refer** → message connects their OH sale to buying in St. Augustine → asks for a
  10-min call → FUB note + buyer stage + task.

## Fixture 3 — Fello home-value, OUT-OF-STATE, NO local intent (REFERRAL)
- **Person:** Susan T. · recently assigned · source: Fello
- **Note (Fello):** "Home Value request — 5 Maple Ct, Austin TX 78701."
- **History:** none; no St. Augustine activity ever.
- **Expected:** out-of-area **and** no local intent → **referral via Revii** → warm
  handoff message, door left open for St. Augustine → FUB note + `Referral – Out of
  Area` tag + referral task.

## Fixture 4 — New portal buyer, after hours (SPEED-TO-LEAD)
- **Person:** Maria L. · created 9:42pm · source: Zillow
- **Note:** "Viewed 2-bed, 210 Oak St, St. Augustine. Requested info."
- **Expected:** brand-new lead → respond **immediately** with a value-first text
  referencing Oak St → offer a weekend showing → FUB note + task. Speed is the point.

## Fixture 5 — Engaged lead, objection (WITH REPLY)
- **Person:** David K. · stage: Engaged
- **Inbound text:** "Thanks but I already have an agent."
- **Expected:** classify = objection (has-agent) → acknowledge, no pressure, add
  value, offer to keep sending matches → continue, don't drop → log note.
- **Turn 2 inbound:** "actually yeah that'd be helpful" → keep nurturing toward a
  call; set cadence.

## Fixture 6 — Fello, ambiguous intent (WITH REPLY)
- **Person:** Pat S. · recently assigned · source: Fello
- **Note (Fello):** "Home value view — no address captured. Opened 'Thinking of
  selling?' email."
- **Expected:** intent unclear → send **one light qualifying question** (sell vs.
  buy/move to St. Augustine) before branching.
- **Turn 2 inbound:** "looking to move to St Augustine next year" → switch to
  relocation-buyer play → offer a no-pressure planning call.

## Fixture 7 — HomeLight seller referral (local)
- **Person:** Greg P. · source: HomeLight · recently assigned
- **Note (HomeLight):** "Seller referral — 47 Marsh Point Dr, St. Augustine. Home
  value request; condition: good; not yet working with an agent."
- **Expected:** detect **HomeLight seller** → offer value range + cash-vs-list
  framing → drive to an in-person valuation appointment (understand goal if possible,
  else just set it) → FUB note + stage to Spoke with Customer/Appointment Set + task.
  Treat as warm/high-priority (paid referral).

## Fixture 8 — Opt-out (RESPONSIBLE STOP, with reply)
- **Person:** Linda H. · stage: Attempted Contact
- **Inbound text:** "Stop. Not interested."
- **Expected:** run the **full opt-out flow** — stop immediately, mark the
  number/email **Do Not Contact**, apply the `Do Not Contact` tag, move to the
  **Fishing Pond**, set stage to Trash, log it. **No further messages.** (Optional
  one-line, compliant sign-off only.)

## Fixture 9 — Existing nurture lead, gone quiet (CONTINUE THE PATH)
- **Person:** Tom & Rae · stage: Spoke with Customer · last touch 23 days ago
- **History:** had a real conversation about 32084 homes $400k; agent sent 2 follow
  ups since, no reply.
- **Expected:** **continue** the cadence (don't restart) → new value angle (e.g., a
  fresh matching listing or market shift), spaced appropriately → callback/appointment
  ask → keep stage Spoke with Customer (or advance if booked) → log. No duplicate of
  prior messages.

---

## Grading
A result **passes** when it: identifies the right lead type/intent, picks the
correct branch (local / referral / qualify), drafts a value-first message with no
"just checking in," makes a callback/appointment ask, and lists the right FUB
updates. Flag anything that refers a relocation buyer, sends a bare "what's your
home worth," or misses the appointment ask.
