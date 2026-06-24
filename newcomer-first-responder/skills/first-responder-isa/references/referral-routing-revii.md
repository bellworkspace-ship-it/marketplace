# Referral routing via Revii

An out-of-area home-value inquiry (e.g., a Fello lead asking about a home in
another state) is not a dead end — it's a referral fee. Route it through the
Newcomer Revii network instead of working it locally.

## When to trigger
- The property the lead is asking about is **outside the agent's service-area
  zips** (from setup), **AND**
- The lead has **no St. Augustine / St. Johns County buy or sell intent**.

Compare the *property* location, not just where the lead lives.

## Qualify intent BEFORE referring (critical)
Do **not** refer just because a valuation address is out of area. Many Fello leads
own a home elsewhere but want to **buy or relocate to St. Augustine** — that's a
local relocation buyer worth keeping, not a referral. First check the notes/history
for St. Augustine intent (see `lead-context-and-fello.md`):
- **Any St. Augustine buy/relocation/sell intent** → keep and work locally; do not refer.
- **Unclear** → ask one light qualifying question first (see the Fello openers in
  `value-message-library.md`).
- **Purely out-of-area, no local intent** → proceed with the referral below (and
  still leave the door open: "if you ever look at St. Augustine, I'm here").

## Flow (browser-driven)
1. **Capture** the referral details from the FUB lead: lead name, contact info,
   the target property/market (city, state, zip), and what they need (buy, sell,
   home value).
2. **Open Revii agent search** in the browser:
   `https://coaching.revii.app/agent-search-home`
   Confirm the agent is logged in; if not, ask them to log in, then resume.
3. **Search** for an agent in the target zip/market. Enter the location and any
   relevant filters the page offers.
4. **Capture the matched agent(s)** — name, brokerage, market, contact details.
5. **Hand off** per the agent's preference from setup:
   - draft an intro/referral message connecting the lead and the receiving agent, and/or
   - create a referral task for the Newcomer agent to approve and send.
6. **Log in FUB**: add a note documenting the referral, tag the lead as
   `Referral – Out of Area`, set stage accordingly, and create a follow-up task to
   track the referral agreement and fee.
7. **Log the outcome** in the team learning log as a referral (see
   `learning-log.md`).

## Rules
- Always confirm the receiving agent/market before connecting anyone.
- Don't promise a specific referral fee to the lead — that's between brokerages.
- Keep the lead warm: tell them you're connecting them with a trusted agent in
  that area, so the experience feels like white-glove service, not a brush-off.
- If Revii returns no match, hold the referral for the agent rather than dropping it.

> Note: Revii (coaching.revii.app) is driven through the browser. If a direct API
> becomes available later, this step can be automated headlessly.
