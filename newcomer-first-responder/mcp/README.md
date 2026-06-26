# Beacon — Follow Up Boss connector (MCP)

This is the **credit-efficient API connection** for Beacon. Instead of browsing the
FUB web UI (expensive), Beacon calls these tools to pull the work list in one shot and
read each lead's full context as compact JSON — using **each agent's own FUB API key**
(scoped to their own leads).

## What it gives Beacon
`whoami`, `list_smart_lists`, `get_work_list` (one bulk call), `get_person` (full
context + recent notes), `list_stages`, `add_note`, `set_stage`, `create_task`,
`create_appointment`, `rate_limit_usage`. (Sending texts still happens in the browser —
FUB's API only logs texts.)

## Requirements
- **Python 3** (already on macOS) and **`pip install fastmcp`** (one time).
- Each agent's **own FUB API key** (FUB → Admin → API). If your account has the *API
  Key Restrictions* power-up on, enable the agent first: **Admin → Teams → API Access**.

## How the key is provided (agent-friendly)
The server looks for the key in this order:
1. `FUB_API_KEY` environment variable, then
2. **`~/.beacon/fub_key`** — a local file Beacon's setup writes for the agent (so they
   never touch env vars). The key stays on the agent's machine; this server never logs
   or stores it.

## Test it yourself first (recommended before publishing)
```bash
pip install fastmcp
mkdir -p ~/.beacon && printf 'YOUR_FUB_API_KEY' > ~/.beacon/fub_key
python3 "/Users/stevenbell/Desktop/TheNewcomerGroup/ClaudePlugins/newcomer-first-responder/mcp/fub_mcp.py"
```
If it starts without error, the wiring is good. Then in Claude, Beacon will have the
`beacon-fub` tools and will prefer them for reading (cheap), falling back to the browser
only for sending. Run **"set up the ISA"** → **"run a test"** and confirm it reads your DB.

> Field-name note: FUB occasionally varies response keys (e.g. `smartlists` vs
> `smartLists`). The server already handles the common cases; if a tool returns empty,
> tell me the endpoint and I'll adjust the parser.

## Two ways to run it for the team
- **Local (default, in this `.mcp.json`):** each agent runs the server on their own
  machine via the plugin. Most secure (key never leaves their device). Needs Python +
  `pip install fastmcp` on each machine.
- **Hosted (optional, less per-agent setup):** host one instance and point agents at it
  (each still sends their own key). Removes the per-machine Python/deps step. Ask me and
  I'll convert this to an HTTP server + give you a one-click deploy (Render/Railway/Fly).

## Turning it on / off
The connection is wired in `../.mcp.json`. If you ever want Beacon back to pure
browser mode, remove that file (Beacon falls back automatically). Bump the plugin
version and republish after changes.
