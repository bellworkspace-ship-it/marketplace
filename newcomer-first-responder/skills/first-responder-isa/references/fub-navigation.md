# Follow Up Boss — browser navigation

How to drive Follow Up Boss through the agent's logged-in browser session using
the Chrome browser tools. The agent's own login scopes everything to their own
leads — no broker credentials are ever used.

## When to use the browser (and when not to)
Do the reliable, structured work through the **API** — detecting leads, reading
context, logging notes, updating stages, creating tasks, and booking appointments
(see `fub-api-reference.md`). Use the **browser only** for:
1. **Sending a text** — FUB's `/textMessages` API only *records* texts, it does
   not send them, so the actual send must go through FUB's texting UI (from the
   agent's number). A 24/7 headless texting provider is a phase-2 upgrade.
2. **UI fallback** — if an API call is unavailable, fall back to the matching
   screen below.

## Before anything
1. Confirm a browser is connected and FUB is open and logged in. If the page
   shows a login screen, stop and ask the agent to log in, then resume.
2. Note the agent's FUB account view (their assigned leads only).

## Find leads that need a touch
Work these FUB views in order:

1. **New / unworked leads** — open the leads list, filter or sort by *Date
   Created* (newest first) and *Stage = Lead/New*. These get worked first.
2. **Newly assigned** — filter the list to leads assigned to the agent within
   the last run window.
3. **Fello inquiries** — if a Smart List exists for Fello home-value views (the
   Fello↔FUB integration syncs Lead Score into a custom field), open it and sort
   by Lead Score, highest first.
4. **Due follow-ups** — open Tasks / the follow-up queue for items due today.

> Setup creates the recommended Smart Lists. If they are missing, fall back to
> filtering the All People list by stage, source, and assignment date.

## Read a lead
Open the lead record and read, top to bottom: the communication timeline (texts,
emails, calls with outcomes), property searches/views, tags, stage, source, and
any Fello fields (score, estimated value, equity, intent). Summarize before
composing.

## Send a text (the core action)
1. On the lead record, open the texting/conversation panel.
2. Type the composed message into the text box.
3. Confirm the destination number is the lead's mobile and that the lead is not
   marked opted-out.
4. Send. Confirm the message appears in the sent timeline.

If a text isn't appropriate (e.g., the lead only gave an email), send via the
agent's connected Gmail instead and log it (next section).

## Book an appointment
1. Confirm proposed times against the agent's Google Calendar.
2. In FUB, create an Appointment on the lead record with date/time/type.
3. Create the matching calendar event and send the lead a confirmation.

## Log activity and advance the lead
After each interaction:
1. Add a **Note** summarizing what was sent/said.
2. Update the **Stage** to reflect reality (e.g., Lead → Engaged → Appointment Set).
3. Create the **next follow-up Task** with a due date per `cadence-rules.md`.

## Guardrails
- Only act within the agent's own logged-in session and assigned leads.
- Never send to opted-out/do-not-contact leads.
- Never send two automated messages to the same lead in one cycle.
- If the UI looks unfamiliar or an element can't be found, stop and report rather
  than guessing — FUB layouts can change.
