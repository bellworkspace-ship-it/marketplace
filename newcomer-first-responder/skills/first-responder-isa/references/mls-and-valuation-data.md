# MLS & valuation data (answer questions without the agent)

To stay hands-off, the ISA must answer real questions — "is it still available?",
"what's the price?", "what's my home worth?" — and send real matches and value
ranges. It does this with **the agent's own data tools**.

## Each agent's tools are set once and remembered
At setup, ask the agent which MLS / valuation tools **they personally have access
to** (e.g., **Paragon**, **RPR / narrpr**, Matrix, Stellar, Zillow, or others) and
store it in their settings — **remember it forever**. Use those tools on every run;
re-ask only if they say it changed.

## How it pulls data
- Each agent has their **own logins**, so drive their tool in the **browser** under
  their session (same approach as comp pulls). The login-dispatch behavior covers
  re-logins (`session-and-login-dispatch.md`).
- If the **`newcomer-cma`** plugin is installed, reuse its skills for accuracy —
  `pull-paragon-comps`, `pull-rpr-comps`, `run-cma`, `market-snapshot` — for
  valuations, comps, and area stats.
- Cache a pulled value/listing briefly within a run so you don't re-pull repeatedly.

## What it answers / sends
- **Buyers:** is a listing active/price/beds-baths/status; send **real matching
  listings** from the agent's MLS for their criteria.
- **Sellers (Fello / HomeLight):** a credible **value range + a driver or two** and,
  when useful, a quick comp set — pulled from the agent's MLS/RPR/CMA.
- **Market questions:** current inventory, days-on-market, price trends for the area.

## Source priority for a value
1. The agent's **MLS / RPR / CMA** (most accurate) →
2. **Fello's** synced estimate (already in FUB) as a fallback/starting point →
3. If neither is available, **ask the agent** or hold — never invent a number.

## Hard rule
**Never invent property facts, prices, availability, or values.** Pull from the
agent's real tool, or ask/hold. Accuracy protects the agent and the lead.
