# Session check & login dispatch

The ISA drives sites in the browser (FUB, Revii). Those sessions log out
periodically. This is the pattern for detecting a logged-out site, alerting the
agent while they're on the go, and recovering with a login dispatch — without
ever mishandling their credentials.

## 1. Session check (start of every run, and before Revii)
Before working, confirm each required site is reachable and logged in:
- **Follow Up Boss** — open it; if a login/SSO screen appears, the session is down.
- **Revii** (`https://coaching.revii.app/agent-search-home`) — only checked when a
  referral is triggered; if it shows a login screen, the session is down.

Also treat as "down": session-expired messages, MFA/2FA prompts, or the expected
page elements being absent.

## 2. If a required site is down → alert the agent on the go
Do not fail silently. Send the agent an alert through the channel they chose in
setup (text to their own number, email, or notification), for example:
> "Newcomer ISA paused — your Follow Up Boss session is logged out, so I couldn't
> work {N} new leads. Reply 'log me in' and I'll handle it, or log in and I'll
> retry on the next run."

Then either pause that part of the run (continue anything that doesn't need the
down site) or stop, and clearly note it in the run summary.

## 3. Login dispatch (agent → Claude)
When the agent dispatches Claude to log in:
1. Retrieve their credentials from the **secure local source** configured in
   setup (OS keychain / password manager / local environment variable / local
   secrets file on the agent's own machine) — or accept credentials the agent
   provides in that moment.
2. Open the site's login page in the browser and enter the credentials into the
   login form.
3. If the site prompts for **MFA/2FA**, ask the agent for the current code in the
   moment and enter it. Never store MFA codes.
4. Confirm login succeeded, then **rerun** the part of the workflow that was
   blocked.

## 4. Credential handling — strict rules
- Credentials are the **agent's own** and live **only on the agent's machine**
  (keychain, password manager, or a local secrets file the agent controls).
- **Never** write credentials into: the plugin/marketplace repo, FUB notes, the
  learning log, run summaries, screenshots, or any chat transcript.
- **Never** transmit credentials anywhere except the site's own login form.
- Prefer keeping sessions persistent to minimize how often login is needed.
- Mask credentials in any output; if you must reference them, refer to "your saved
  {site} login," not the values.

## 5. Reduce how often this happens
- Encourage agents to keep FUB and Revii logged in / "remember me" on their
  working browser.
- Run the schedule during working hours when the browser is typically open.
- For true 24/7 unattended sending, the phase-2 texting provider removes the
  browser-session dependency for the send step (see plugin README).
