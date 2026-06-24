# Value-first message library

Every outbound message carries exactly **one** concrete value item. If you can't
name the value in one sentence, don't send it. "Just checking in," "touching
base," and "any updates?" are banned.

## The five value types (pick the best fit for the lead)

### 1. Matching listing
A specific new or relevant listing that fits their search.
> "A 3-bed just hit in {neighborhood} at {price} — bigger backyard than the last
> ones you looked at. Want me to send the full details or line up a showing?"

### 2. Home-value / equity update (great for Fello & seller leads)
A real number tied to their home or interest, pulled from the CMA tools or the
Fello data in FUB.
> "Quick one — homes like yours on {street} are now running about {value}, up
> roughly {pct} since you last checked. Want the full breakdown of what's driving
> it?"

### 3. Market stat that affects their decision
A specific, current local data point with a "so what."
> "Inventory in {area} jumped {n}% this month, which usually means more room to
> negotiate. If you've been waiting for leverage, this is it — want to talk
> timing?"

### 4. Direct answer to their last question
Always answer an open question before anything else. Pull the real answer; never
guess on price/terms.

### 5. Helpful resource / next step
A genuinely useful tool: a saved search, a neighborhood guide, a lender intro, a
home-value report link.
> "Set you up a live alert for {criteria} so you see new {area} listings the
> minute they post — want me to turn it on?"

## Construction rules
- **One value item per message.** Don't stack three.
- **Reference something specific to this lead** (a property they viewed, a
  neighborhood, a prior message). Generic = ignored.
- **End with one low-friction ask** that moves toward a call or appointment.
- **Keep it short** — text length, not an essay. See `message-style-guide.md`.
- **Pull real data.** Listings, prices, and stats must come from real sources
  (MLS / CMA tools / Fello), not invented.
- **Check the learning log first** (`learning-log.md`) and favor value types and
  angles that are converting for the team right now.

## First-touch templates by lead source
- **Portal/buyer lead (Zillow, etc.):** acknowledge the exact property/search,
  offer one matching listing or a saved search, ask a qualifying question.
- **HomeLight (seller referral):** acknowledge their HomeLight request, offer a real
  value range or cash-vs-list framing, and drive to an in-person valuation
  appointment — understand their goal if you can, otherwise just set the appointment.
  Full openers in `homelight.md`.
- **Sphere/referral:** warmer tone, reference the mutual connection, offer help
  with no pressure.

## Fello first-touch openers (goal: a callback or appointment)
Read the inquiry note + history first (see `lead-context-and-fello.md`). Keep it
light, human, and aimed at a quick call — not a hard sell. Examples:

**Local home-value inquiry (St. Augustine / St. Johns County address):**
> "Hi Karen — saw you were checking values around {neighborhood}. Quick read:
> homes like yours are running ~{value} right now. Happy to walk you through what's
> driving it on a 5-min call — are you weighing a possible move, or just keeping an
> eye on it?"

**Cash-offer inquiry:**
> "Hi {first} — you'd looked into a cash offer on {street}. I can get you real
> numbers (cash vs. listed, net to you). Want me to pull those together and call you
> this week?"

**Relocation buyer (out-of-area home, but St. Augustine intent in their history):**
> "Hi {first} — looks like you were eyeing the St. Augustine area a while back and
> just checked your {currentcity} home's value. If you're thinking about making the
> move, I can line up homes here that fit and time it with your sale. Want to grab
> 10 minutes this week?"

**Ambiguous intent (qualify in one light question):**
> "Hey {first} — saw your home-value request come through. Quick one so I point you
> the right way: are you thinking about selling, or looking to buy/move to the St.
> Augustine area?"

**Out-of-area, no St. Augustine intent (warm referral handoff):**
> "Hi {first} — for a {city} valuation I'd rather connect you with a great agent I
> trust right in that market so you get an accurate number. I'll make the intro
> today. And if you ever look at St. Augustine, I'm here." → then run
> `referral-routing-revii.md`.

Rules for Fello touches: one value item, one easy ask, push toward a **call or
appointment**, and never send a bare "what's your home worth?" — you already know
they asked; acknowledge it and add value.
