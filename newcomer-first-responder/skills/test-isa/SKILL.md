---
name: test-isa
description: >
  This skill should be used to test the Newcomer First Responder ISA and show the
  agent the results, without them having to create real leads or send real texts.
  It has a zero-setup simulation mode (runs the ISA on built-in sample leads and
  reports exactly what it would do) and an optional one-text live sandbox mode.
  Triggers on "run a test", "test the ISA", "show me a test run", "does this work",
  "simulate leads", "test the first responder", or "prove it works".
metadata:
  version: "0.1.0"
  author: "The Newcomer Group"
---

# Test the Newcomer ISA

Goal: let the agent verify the ISA works **without doing the testing themselves**.
Default to the simulation — it needs no setup, touches nothing real, and shows
results immediately. Offer the live sandbox only if they want a real text to their
phone.

## Mode 1 — Simulation (default; zero setup, nothing real is touched)
Do **not** call Follow Up Boss or send anything in this mode. Instead:

1. Load the sample leads in `references/test-fixtures.md`.
2. For **each** sample lead, run the real ISA decision loop and report:
   - **Detected type** (e.g., Fello home-value, relocation buyer, new portal buyer).
   - **Intent read** — the one-line read from the notes/fields/history.
   - **Branch chosen** — work locally / referral / qualify-first / objection handling.
   - **Message drafted** — the exact text the ISA would send (applying the
     value-first and style rules).
   - **FUB actions it would take** — note logged, stage change, task, appointment.
   - **The ask** — the callback/appointment move.
3. For the two fixtures marked "with reply," run **one or two back-and-forth turns**
   to show objection handling and how it drives to an appointment.
4. **Self-grade** each result against the fixture's "Expected" checklist and mark
   ✓ pass / ✗ needs-attention with a one-line reason.
5. Present a clean **Test Results** summary (offer to save it as a file the agent
   can keep). End with an overall pass/fail and any notes.

Keep the output skimmable: one compact block per lead. This is the fast way for
the agent to confirm the logic — read it in two minutes, no work required.

## Mode 2 — Live sandbox (only if the agent asks AND FUB is connected)
Proves the real integration end-to-end with a single real text to the agent's own
phone. Strict guardrails.

1. Confirm the agent's **own** mobile number (never anyone else's).
2. Create a clearly-labeled test lead in FUB: name **"ZZ TEST — Newcomer ISA"**,
   the agent's own number/email, and add a synthetic **Fello home-value inquiry
   note** (use one from the fixtures).
3. Run the real loop on that one lead only: read it, draft, **send exactly ONE
   real text** to the agent's phone, propose a time and book a **test appointment**,
   and log the note/stage to FUB.
4. Show the agent what happened (the text they should have just received, the
   appointment created, the FUB updates).
5. **Clean up:** tag the lead `TEST`, and offer to delete the test lead and test
   appointment so nothing lingers.

**Live-mode rules:** only the agent's own number; exactly one outbound text; every
artifact labeled TEST; never touch any real lead; always offer cleanup.

## After any test
Summarize pass/fail in plain language and, if anything looked off (voice, branch,
or ask), offer to adjust the relevant playbook and re-run.
