# Routing, dedup & no-double-text

Newcomer leads are **auto-routed** to agents (FUB lead flow / round-robin), so the
ISA works leads **already assigned** to the agent. The job here is to make sure a
lead is never messaged twice and to handle data gaps cleanly.

## Assignment
- Work only the agent's **assigned** leads (auto-routing handles delivery).
- Optional safety net (if the agent enables it in setup): also check unclaimed/pond
  leads they're allowed to claim. Otherwise, ignore unassigned leads.
- If a lead was **reassigned away** from the agent, stop working it.

## One conversation per lead (no double-text)
The First Responder and Nurture skills must never both message the same person.
Enforce all of these:
1. **Divide by lead state.**
   - *First Responder* owns **brand-new / just-assigned** leads and any **active live
     thread** (lead replied or is mid-conversation).
   - *Nurture* owns **established pre-appointment stages** (Attempted Contact, Spoke
     with Customer) and **older** leads with no active thread.
2. **Shared cooldown.** Never message a lead that **either** skill touched within the
   cooldown window (default ~12h for nurture; live threads respond in real time).
3. **Ownership marker.** When a skill sends a touch, log it (note + a "last ISA
   touch" timestamp, and an `ISA:Active` tag while a thread is live). The other skill
   **skips** leads touched this cycle or owned by an active thread.
4. **Live conversation wins.** If a lead is mid-exchange, only the skill handling
   that thread acts; the other defers.

## Dedup (same person, multiple sources)
- Before treating a contact as new, run `GET /people/checkDuplicate`.
- If the same person exists from multiple sources (Fello + Zillow + DB), treat them
  as **one** conversation — never run parallel threads.

## Contact-data fallbacks (don't stall silently)
- **No mobile** → use email instead.
- **Landline or invalid number** → never text it; try email; flag for the agent.
- **No phone and no email** → flag the lead for the agent; don't loop on it.
- Always pick the channel the lead has actually engaged on before.

## Rules
- One lead = one conversation = one channel at a time.
- Respect the cooldown and ownership markers on every run.
- Never text a landline, invalid, or opted-out number.
