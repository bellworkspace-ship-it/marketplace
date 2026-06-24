# Scheduling & booking (the hands-off finish line)

The whole system exists to get a **call or appointment on the calendar** without the
agent lifting a finger. Book the right slot, never double-book, and send a real
invite.

## Read real availability first
- Pull the agent's **Google Calendar** free/busy before proposing any time.
- Load the agent's booking rules from setup: appointment hours, buffers, travel
  time, max appointments/day, preferred windows, and minimum lead time (e.g., don't
  offer a slot less than ~2 hours out).
- **Never offer a time that conflicts** with an existing event.

## Appointment types & durations (from setup)
Match duration and format to the appointment type, e.g.:
- **Phone call / callback** — 15 min, video or phone.
- **Buyer consult** — 30 min.
- **Listing / valuation appointment (in-person)** — 60 min + travel buffer.
- **Showing** — 30 min + travel buffer.
Use the types/durations the agent configured; default sensibly if unset.

## Offer & confirm
1. Offer **2–3 concrete open slots** (not "what works for you?").
2. On a pick, **book it**: create the appointment in FUB (`POST /appointments` with
   the type) **and** a Google Calendar event.
3. **Invite the lead** (add them as a guest so they get the invite), include the
   **location** for in-person/valuation or a **video/phone link** for calls.
4. Send a short **confirmation** text/email with the day/time and what to expect.
5. Move the lead to **Appointment Set** and notify the agent (see
   `escalation-alerts-autonomy.md`).

## Time zones (relocation buyers!)
Detect the lead's time zone (area code / address / relocation context) and **propose
times in their zone**, while booking the agent's calendar in the agent's zone. State
the zone explicitly ("2pm your time / 3pm mine").

## Reschedule & cancel (stay hands-off)
- "Can we move it?" → offer new open slots, update **both** FUB and the calendar,
  re-confirm.
- Cancellation → free the slot, set a follow-up task, and gently offer to rebook.
- Always keep FUB and the calendar in sync.

## Reduce no-shows (light touch)
Send a confirmation at booking and a brief reminder the day before / morning of.
Keep it to value + logistics, never nagging.

## Rules
- Never double-book or offer a busy slot.
- Never book outside the agent's appointment hours/rules.
- Always send the invite + confirmation; always update FUB stage + calendar together.
- If the calendar can't be read, don't guess — alert the agent rather than risk a
  bad booking.
