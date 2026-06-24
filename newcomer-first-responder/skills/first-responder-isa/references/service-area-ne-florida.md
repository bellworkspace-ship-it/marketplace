# Service area — Northeast Florida (preloaded)

The agent's service area is **preloaded to this exact zip list** — agents do not
enter zip codes. Use it to decide **local vs. out-of-area** for referral routing and
relocation-buyer detection. Home base is **St. Augustine / St. Johns County**.

## The rule
A property is **LOCAL** if its zip code is in the list below. Otherwise it's
**out-of-area** — apply the intent gate first (`referral-routing-revii.md`): if the
lead has NE Florida buy/sell intent (e.g., a relocation buyer moving here), keep and
work locally; only refer if there's no local intent.

## Service-area zip codes (62)

**Nassau — Amelia Island / Fernandina Beach / Yulee / Callahan / Hilliard / Bryceville**
`32009, 32011, 32034, 32035, 32041, 32046`

**Duval — Jacksonville + beaches (Atlantic Beach, Jacksonville Beach, Neptune Beach)**
`32202, 32204, 32205, 32206, 32207, 32208, 32209, 32210, 32211, 32212, 32214,
32216, 32217, 32218, 32219, 32220, 32221, 32222, 32223, 32224, 32225, 32226,
32227, 32233, 32234, 32244, 32246, 32250, 32254, 32256, 32257, 32258, 32266`

**St. Johns — St. Augustine / Ponte Vedra / Nocatee / St. Johns (Fruit Cove, Julington Creek, RiverTown) / Hastings**
`32080, 32081, 32082, 32084, 32086, 32092, 32095, 32145, 32259`

**Clay — Orange Park / Fleming Island / Middleburg / Green Cove Springs / Doctors Inlet / Penney Farms**
`32003, 32006, 32030, 32043, 32050, 32065, 32067, 32068, 32073, 32079`

**Flagler — Palm Coast**
`32135, 32137, 32142, 32164`

## Notes
- This is the authoritative coverage list. To add or remove an area, edit this file
  (then `build.sh` → `verify.sh` → push).
- The zip determines local vs. out-of-area; the county/area labels above are for
  readability and message personalization.
