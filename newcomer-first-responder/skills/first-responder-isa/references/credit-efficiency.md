# Credit efficiency (least credits, high quality, max reach)

Beacon runs on the agent's own Claude, so every run spends their credits. Priorities,
in order: **quality**, **reach** (touch every lead that needs it), **low cost**.
Speed does not matter. Follow these rules to spend the fewest tokens for the most
high-quality touches.

## The golden rule
**Read cheaply, think only where it counts.** Most cost is in (a) fetching data and
(b) composing messages. Minimize both: pull data in bulk once, triage cheaply, and
only spend "thinking"/composition tokens on leads that will actually get a touch.

## Reading the database (who to work)
1. **Pull the work list in ONE bulk call** — the smart list / filtered people list.
   Get who's due in a single structured response. **Never** re-query per lead to
   build the list.
2. **Prefer the FUB API for all reading** (structured JSON is far cheaper and
   cleaner than rendering web pages). Use the browser to *read* only if no API
   connection is configured — and then read **text** (`get_page_text`), never
   screenshots.
3. **Cheap triage before deep reads.** From the list, drop opted-out, protected,
   already-messaged-this-cycle, and not-yet-due leads **without** opening them. Only
   the survivors get a full-context read.

## Reading a lead's full context (quality — do this for every lead you work)
- Read the lead's **full profile in the fewest calls**: stage, notes, last
  messages/calls, property activity, Fello/HomeLight fields. This is required for a
  good re-approach — but pull it **once**, compactly, and reuse it for the whole
  decision (read → decide → compose) without re-fetching.
- Don't pull more history than you need to choose the next touch.

## Composing & sending
- **One worked lead = one compose.** Spend composition tokens only on leads getting a
  message; keep messages short (texts, not essays).
- **The browser is the expensive part — use it only to SEND**, once per message.
  Never browse to read data when the API can.
- **Batch writes** (notes, stage updates) where possible.

## Reach within a budget (per-run caps)
- Work a **capped number per run**, prioritized: replies first, then new/hot, then
  most-overdue. Spread the rest across the next scheduled runs.
- This guarantees the highest-value leads are reached first, and **everyone gets
  covered over time** without one giant expensive run. Slow and steady = full reach
  at low cost.

## Don't re-do solved work
- Skip leads already handled by checking last-touch/stage **cheaply** (from the bulk
  list), without re-reading the whole profile.
- Keep the per-run "already touched" markers so reads/composes never repeat.

## Quick checklist each run
1 bulk list call → cheap triage → full read only on survivors (capped) → one compose
each → send via browser → batch-log → stop at cap, resume next run.
