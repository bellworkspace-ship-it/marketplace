# Stage workflow (standard FUB model)

Newcomer uses the standard out-of-the-box Follow Up Boss stages. Keep every lead in
the right stage so follow-up stays organized and nothing slips. **Read the live
stages first** so this adapts to the account exactly.

## Read the account's stages
Call `GET /stages` and use the actual stage names. Map by meaning to the working
flow below; if a name differs, match the closest equivalent.

## The pre-appointment working flow (what this system drives)
```
New / Lead
   → Attempted Contact      (reached out, no two-way connection yet)
   → Spoke with Customer    (had a real two-way conversation)
   → Appointment Set        (a listing appt, showing, or consult is booked)
```
Common related stages: **Unknown** (attempted, no connection, timeline unclear),
**Nurture** (longer-horizon), **Hot Prospect** (high intent). Later stages
(Active Client, Pending, Closed, Past Client, Sphere, Trash) are out of scope for
this system except **Trash** for opt-outs.

## When to move a lead
- **→ Attempted Contact:** an outbound touch was made but no reply/connection yet.
- **→ Spoke with Customer:** the lead replied and a real two-way exchange happened.
- **→ Appointment Set:** a call/valuation/showing/listing appt is on the calendar.
  (Appointment Set = any booked appointment, listing or showing.)
- **→ Nurture:** engaged but long-horizon; keep value touches at a slower cadence.
- **→ Trash + Fishing Pond:** opted-out / Do Not Contact (see
  `opt-out-and-compliance.md`).

## Rules
- Update the stage via `PUT /people/:id` right after the interaction that changed it.
- Never skip a lead because of its stage — Attempted Contact and Spoke with Customer
  are exactly the leads this system must keep working until an appointment is set.
- Don't move a lead backward (e.g., out of Appointment Set) without a clear reason
  (e.g., a cancellation) — log the reason.
- Keep stage changes consistent so Smart Lists and reporting stay accurate.
