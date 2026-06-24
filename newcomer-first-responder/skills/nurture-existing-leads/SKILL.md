---
name: nurture-existing-leads
description: >
  This skill should be used to follow up with EXISTING and older leads already in
  Follow Up Boss — not brand-new inquiries — and move them toward a set
  appointment. It works leads in the agent's pre-appointment stages (e.g.
  Attempted Contact, Spoke with Customer), continues the follow-up path already
  started, replies by text or email, handles replies, and responsibly handles
  opt-outs. Runs on a 3×/day schedule. Triggers on "nurture my leads", "work my
  existing leads", "follow up with my database", "work my attempted-contact leads",
  "work my spoke-with-customer leads", "work my older leads", or its scheduled run.
metadata:
  version: "0.1.0"
  author: "The Newcomer Group"
---

# Nurture existing & older leads

Keep every in-progress and older database lead moving toward a booked appointment —
continuing the follow-up the agent already started, never restarting it, and always
responsibly. Same engine, voice, and value-first rules as the First Responder ISA;
this skill applies them to leads already in the pipeline. Runs **3× per day**.

This skill shares the First Responder's playbooks. Use the files in
`skills/first-responder-isa/references/`: `fub-api-reference.md`,
`error-handling-and-resilience.md`, `message-style-guide.md`, `objection-playbook.md`,
`cadence-rules.md`, `value-message-library.md`, `lead-context-and-fello.md`,
`homelight.md`, `opt-out-and-compliance.md`, `stage-workflow.md`,
`scheduling-and-booking.md`, `routing-and-dedup.md`, `mls-and-valuation-data.md`,
`escalation-alerts-autonomy.md`, `session-and-login-dispatch.md`,
`referral-routing-revii.md`, `fub-navigation.md`, and `learning-log.md`. Apply them
the same way the First Responder does — booking, no-double-text, real data, and
escalation all apply here too.

## Operating principles (responsible & controllable)
1. **Continue, don't restart.** Read what the agent has already done and pick up
   the cadence from there — never duplicate or spam a lead.
2. **Value every time, never "just checking in."** Same rule as First Responder.
3. **Honor opt-outs instantly.** "Stop"/"not interested" → run the full opt-out flow
   and stop forever. See `opt-out-and-compliance.md`.
4. **Controlled volume.** Respect the per-run cap, frequency caps, quiet hours, and
   rate limits. Re-engage older leads gently, not in a blast.
5. **Right stage, always.** Keep each lead in the correct FUB stage. See
   `stage-workflow.md`.
6. **The agent's lane only.** Their own assigned leads, the sanctioned actions only.

## The loop (run 3× per day)

### 1. Session & setup
Confirm FUB API access and the browser for sending (login-dispatch if a site is
logged out). Load the agent's quiet hours, per-run cap, and the configured
**Fishing Pond** from setup.

### 2. Read the account's stages
Call `GET /stages` to get the agent's actual stage names (they use the standard
out-of-the-box model). Identify the **pre-appointment working stages** — primarily
**Attempted Contact** and **Spoke with Customer** (plus similar like Contacted,
Nurture, Unknown) — and the target, **Appointment Set**.

### 3. Build the work queue (with caps, in priority order)
1. **Leads who replied** since the last run — handle first.
2. **HomeLight seller leads** needing an appointment (`homelight.md`).
3. **Due follow-ups** in Attempted Contact / Spoke with Customer.
4. **Older / overdue leads** worth a gentle re-engagement (oldest meaningful first).

Apply the per-run cap and pace to respect rate limits
(`error-handling-and-resilience.md`). Skip opted-out/DNC, anyone messaged this
cycle, and anyone a human is actively working.

### 4. Read each lead's history (continue the path)
Read prior notes, texts, calls, and stage history. Determine: what's been tried,
the last touch and channel, the last open question, and the next logical step in
the cadence (`cadence-rules.md`). Never repeat a prior message.

### 5. Handle replies first
- **Opt-out** ("stop", "not interested", "remove me", "unsubscribe", "don't
  contact") → run `opt-out-and-compliance.md` (mark the number/email Do Not
  Contact, apply the Do Not Contact tag, move to the Fishing Pond, log) and STOP.
- **Objection / question** → `objection-playbook.md`.
- **Positive / ready** → move toward booking now.

### 6. Choose channel + compose
Pick the **best channel for this lead** — text or email — based on what's worked
before and what's available. Compose the next value-first touch that *continues*
the sequence (new angle each time), aimed at a callback or appointment.

### 7. Send & log
Send the text through FUB's UI (browser) or the email via the agent's Gmail, then
log it via the API (`POST /notes`). Never drop a log.

### 8. Stage hygiene
Advance the lead per `stage-workflow.md`: a real two-way conversation → **Spoke
with Customer**; attempts with no connection → **Attempted Contact** (or Unknown);
booked → **Appointment Set**; opted-out → handled by the opt-out flow.

### 9. HomeLight leads
These are seller valuation / cash-offer referrals. **First try to understand what
they want** (valuation, cash offer, timeline, condition); **if you can't, just work
to set the appointment.** Follow up persistently until they respond. See
`homelight.md`.

### 10. Log outcomes & report
Append anonymized outcomes to the team learning log. End with a summary: leads
worked, texts/emails sent, replies handled, appointments set, opt-outs processed,
and anything held for the agent.

## Guardrails
- Never contact an opted-out/DNC lead or a number on the Do Not Call list.
- Respect quiet hours, the per-run cap, and frequency caps (don't over-message,
  especially older leads).
- Continue the existing cadence — never restart or double-message.
- Hold anything sensitive (legal, complaint, major life event) for the agent.
- Operate only on the agent's own assigned leads, with the sanctioned actions.
