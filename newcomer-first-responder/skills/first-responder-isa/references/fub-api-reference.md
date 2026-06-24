# Follow Up Boss API reference (authoritative)

Use the **API** for everything structured and reliable (detect, read, log, book,
update). Use the **browser** only for the one thing the API can't do — actually
*sending* a text — plus the Revii referral search. This API-first design is what
keeps the ISA from throwing integration errors.

> Canonical live source (check if anything here seems off, FUB updates it):
> API reference index → https://docs.followupboss.com/reference/getting-started
> Machine-readable index + OpenAPI → https://docs.followupboss.com/llms.txt

## Base
- Base URL: `https://api.followupboss.com/v1/` — HTTPS only, version `v1`.
- Resources are plural: `/people`, `/events`, `/notes`, etc.

## Authentication (per agent, scoped to that agent)
Two options:
- **OAuth (preferred, lowest-friction):** agent clicks "Connect" and consents; the
  app gets a Bearer token. Use `Authorization: Bearer <token>`. Best for
  non-technical agents — no key copying.
- **API key (fallback):** agent's key from **Admin → API**. HTTP Basic auth — key
  as username, blank password.

**Scope is automatic and safe:** a key/token has the *same access as the user it
belongs to*. An **Agent**-role user can only see/act on **their own assigned
contacts** — never the whole brokerage. Permission levels:
- **Owner** — everything; only role that can manage **webhooks**.
- **Admin/Broker** — most things, but not webhooks.
- **Agent** — only assigned/collaborator contacts; restricted action plans.
- **Lender** — even less.

Put agents on the **Agent** role. Never distribute the Owner/Admin key.

## System identification (broker does once)
Register the integration once at https://apps.followupboss.com/system-registration
to get **`X-System`** and **`X-System-Key`**. Send both headers on **every**
request:
```
X-System: NewcomerAI
X-System-Key: <key>
```
Why it matters: required by FUB to provide services to customers, and it **more
than doubles the rate limits** (global 250 vs 125 per window). Without it the ISA
will hit limits fast. ("system" = the software; not the lead "source".)

## Which endpoint for which ISA action
**Detect leads**
- `GET /people` — filter by stage, assignment, created date (newest first).
- `GET /events` — inbound lead activity (limit: 20 / 10s).
- `GET /smartLists` + `GET /smartLists/:id` — read the agent's "New Leads" /
  "Fello" lists.
- `GET /me`, `GET /identity` — confirm the authenticated agent + scope.

**Read context**
- `GET /people/:id` — full person (stage, tags, source, custom/Fello fields).
- `GET /textMessages`, `GET /calls`, `GET /events` — communication history.
- `GET /people/checkDuplicate` — avoid creating duplicates.

**Act / log (keep FUB current)**
- `POST /notes` — log every message/call (limit: 10 / 10s).
- `PUT /people/:id` — update stage/fields (limit: 25 / 10s).
- `POST /tasks`, `PUT /tasks/:id` — set/clear the next follow-up.
- `POST /appointments` (+ `GET /appointmentTypes`, `POST /appointmentOutcomes`)
  — book and record outcomes.
- `POST /events` — register a new lead/activity (unlimited; works even if the
  account is in grace/expired state).

**Send the message**
- ⚠️ `POST /textMessages` **logs only — it does NOT send a text.** To actually
  send, drive FUB's texting UI in the browser (`fub-navigation.md`) or use the
  phase-2 texting provider. Email may go via the agent's connected Gmail.

**Nurture automation (optional / phase-2 send path)**
- `GET /actionPlans`, `POST /actionPlansPeople` — enroll a lead into a value-based
  plan that FUB executes.
- `GET/POST /textMessageTemplates`, `/templates` — reusable templates with merge
  fields.

**Referrals & org**
- `GET /users`, `GET /teams`, `GET /ponds`, `GET /groups` (+ `/groups/roundRobin`).

**Detection infra (broker-owned)**
- `POST /webhooks` (Owner only) — e.g. `peopleCreated`, `peopleStageUpdated`,
  `notesCreated` for near-real-time detection. Steven sets these up centrally.

**Rate-limit self-monitoring**
- `GET /rateLimit/usage`, `GET /rateLimit/limits` — see `error-handling-and-resilience.md`.

## Full resource list (for reference)
events · people (+checkDuplicate, unclaimed, claim, personAttachments) ·
peopleRelationships · identity · notes · calls · textMessages · users (+/me) ·
smartLists · actionPlans (+actionPlansPeople) · automations (+automationsPeople) ·
templates · textMessageTemplates · emEvents · emCampaigns · customFields · stages ·
tasks · appointments · appointmentTypes · appointmentOutcomes · webhooks ·
webhookEvents · pipelines · deals (+dealCustomFields, dealAttachments) · groups ·
teams · teamInboxes · ponds · inboxApps · reactions · threadedReplies · timeframes ·
rateLimit.
