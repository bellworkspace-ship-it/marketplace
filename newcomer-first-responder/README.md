# Newcomer First Responder ISA

An always-on AI inside sales agent for Newcomer Group agents. It uses the
**Follow Up Boss API** to find new, unworked, and newly assigned leads, read full
context, log activity, update stages, and book appointments — and the **browser**
only to send value-first texts (FUB's API can't send them) and run Revii referral
searches. It handles objections, self-heals on rate limits and errors, learns
across the team, and runs on **each agent's own Claude** (their credits), so it
costs the brokerage nothing to operate. It works **both** brand-new leads (First
Responder) **and** the existing/older database (nurture, 3× a day), covers **Fello**
and **HomeLight** lead sources, and handles **opt-outs** responsibly.

## What it does

- **Speed-to-lead:** works new leads the moment they appear, day or night.
- **Value-first messaging:** every text carries one real value item — a matching
  listing, a home-value/equity update, a market stat, or an answer. Never "just
  checking in."
- **Conversational & objection-aware:** reads each reply and responds from a
  playbook, always adding value, moving toward an appointment.
- **Adaptive cadence:** tightens for responsive leads, spaces out and switches
  angle for quiet ones.
- **Books appointments:** into FUB and the agent's Google Calendar.
- **Keeps FUB current:** logs notes, advances stages, sets next-touch tasks.
- **Referral routing:** out-of-area inquiries go to Revii to find an agent in
  that market — turning a dead lead into a referral fee.
- **Gets smarter over time:** a shared, anonymized team learning log surfaces
  what's converting so every agent benefits from the whole team's results.

## Components

- **Skill: `first-responder-isa`** — the core loop (detect → read → compose →
  send → book → log → learn) with reference playbooks for the authoritative FUB
  API, error-handling/resilience, FUB browser navigation, the value-message
  library, message voice, objection handling, cadence, Fello/lead context, Revii
  referral routing, the session/login-dispatch pattern, and the team learning log.
- **Skill: `nurture-existing-leads`** — works **existing and older** leads (not new
  inquiries) toward an appointment. Runs **3× a day**, continues the follow-up the
  agent already started, replies by best **text or email**, manages standard FUB
  stages (Attempted Contact → Spoke with Customer → Appointment Set), and handles
  **opt-outs** responsibly (Do Not Contact tag, mark the number/email, move to the
  Fishing Pond). Handles **HomeLight** seller referrals.
- **Skill: `setup-newcomer-isa`** — one-time onboarding wizard (connections,
  service area, hours, voice, alerts, secure login, learning log, schedule).
- **Skill: `test-isa`** — proves it works without you doing the testing. A
  zero-setup **simulation** runs the ISA on built-in sample leads and reports every
  decision and drafted message (self-graded), plus an optional **one-text live
  sandbox** to your own phone.

## Setup

**Broker (one time):** register the system for the `X-System` key, enable the API
Key Restrictions power-up, create owner-level webhooks, and set up the shared team
learning log. Agents inherit all of it.

**Agent (~2 minutes):** run **"set up the ISA"** → click **Connect Follow Up Boss**
(one-click OAuth), connect Google Calendar + Gmail, confirm Chrome has FUB and
Revii logged in (for the text-send + referral steps), and set a few preferences
(service area, hours, voice, alert channel). The ISA then schedules itself.
Finish with a **dry run** that drafts (doesn't send) so you approve the voice.

Then it runs automatically. You can also say **"work my new leads"** anytime.

## Testing it

Say **"run a test"**. The ISA runs in **simulation mode** against built-in sample
leads (local Fello valuation, relocation buyer, out-of-area referral, after-hours
buyer, an objection, an ambiguous Fello inquiry) and reports the type, intent,
branch, and exact message for each — self-graded pass/fail. No real leads, no
texts, nothing for you to set up. For a real end-to-end check, say **"run a live
test"**: it creates a labeled test lead with your own number, sends exactly one
real text to your phone, books a test appointment, and offers to clean up.

## Staying hands-off until the call/appointment is booked

The suite closes the loop from lead-in to booked without the agent:

- **Smart scheduling & booking** — reads real calendar availability, respects
  appointment types/durations, buffers, time zones, and minimum lead time;
  conflict-checks; sends the lead a calendar invite; and auto-reschedules.
- **No double-text** — First Responder and Nurture coordinate (ownership markers +
  cooldown) so a lead never gets two messages; duplicates are merged; missing/landline
  numbers fall back to email or get flagged.
- **Real property & value answers** — uses each agent's own MLS/valuation tools
  (Paragon, RPR, etc., set once and remembered) to answer listing/value questions and
  pull real comps, reusing `newcomer-cma` when installed.
- **Escalation, alerts & autonomy** — clear human-handoff triggers (upset, legal,
  "is this a bot?", call-me-now, VIP), a context brief for the agent, immediate pings
  for the moments that matter, and an Approve-vs-Auto autonomy dial per agent.

## How access is controlled (important)

- Each agent connects with their **own** scoped access — **OAuth** (preferred) or
  an **Agent-role API key**. Either way the ISA can only see/act on **that agent's
  assigned leads**, never broker-wide data.
- The broker registers Newcomer AI as one **system** (`X-System`) — this raises
  rate limits and is required by FUB; it carries no per-agent data access.
- The **API Key Restrictions** power-up lets the Owner grant/revoke each agent's
  access centrally (instant kill switch).
- The plugin only performs the specific actions defined in the skill (read leads,
  log notes, update stage, create tasks, book appointments, send a text, create
  referrals), and **self-heals** on rate limits and transient errors.

## Credentials & privacy

- Login credentials stay **only on the agent's own machine** (keychain, password
  manager, or a local secrets file). They are never stored in this plugin, in
  FUB, in the learning log, in run summaries, or in any shared location.
- The team learning log is **anonymized** — outcomes and categories only, never
  lead names, numbers, emails, or addresses.

## Sending channel (v1) and the phase-2 upgrade

v1 sends texts by driving FUB's texting UI in the browser, so messages go out
from the agent's own number (FUB's API only *logs* texts, it can't send them).
This needs the agent's browser open/connected, so it's ideal during working
hours. **Phase 2:** add a 10DLC-registered texting provider for true 24/7
unattended sending (and optionally a FUB webhook relay for instant, sub-minute
response).

## Distributing to the team

This plugin can be installed directly from its `.plugin` file. To distribute
across Newcomer, host it in a **private plugin marketplace** (a private git repo
with a `.claude-plugin/marketplace.json`). Agents add it once with
`/plugin marketplace add <your-org/your-repo>` and install with
`/plugin install newcomer-first-responder`. Push an update to the repo and every
agent gets it automatically.

## Companion plugin (planned)

**Sphere & Past-Client Nurture** — a warmer, relationship-first plugin that keeps
past clients and sphere contacts engaged for repeat and referral business. It
reuses this engine and the same FUB + learning-log foundation.
