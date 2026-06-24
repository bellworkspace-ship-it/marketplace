# Publishing Newcomer AI to your team

You have two ways to get this into your agents' Claude. Use whichever fits.

---

## Option A — Just send the file (fastest, no website)
Good for a quick pilot or a couple of agents.

1. Send each agent the **`newcomer-first-responder.plugin`** file.
2. They open it with Claude and click **Install**. Done.

Downside: updates mean re-sending the file. For the whole team, use Option B.

---

## Option B — Host a private marketplace (best for the team) ✅
A "marketplace" is just a **private GitHub repo** that holds the plugin. Agents add
it once; after that they install in one click and get every update you push
automatically. This folder (`newcomer-ai-marketplace/`) is already a ready-to-publish
marketplace.

### One-time, by you (about 10 minutes)
1. Create a **free GitHub account** if you don't have one, and make a **new private
   repository** named e.g. `newcomer-ai`.
2. Upload the **contents of this `newcomer-ai-marketplace/` folder** to that repo
   (drag-and-drop in GitHub's "Add file → Upload files" works, or use git). The repo
   root must contain the `.claude-plugin/` folder and the `newcomer-first-responder/`
   folder.
3. Give your agents access to the repo (invite them as collaborators, or make the
   repo internal to your org).

That's it — your marketplace is live.

### One-time, by each agent (in the Claude desktop app)
The `/plugin ...` slash commands only work in the Claude Code CLI — **desktop
(Cowork) agents use the UI**:
1. Claude desktop → **Cowork** tab → **Customize** → **Plugins** tab.
2. **Personal plugins** → **+** → **Add marketplace** → **Add marketplace from GitHub**.
3. Paste: `https://github.com/bellworkspace-ship-it/marketplace`
4. Install **newcomer-first-responder**.
5. Type **"set up the ISA"** → then **"run a test."**

> Private-repo note: agents need read access to it. If that's friction for
> non-technical agents, use a dedicated **public** repo (the marketplace holds only
> plugin instructions — markdown prompts, no secrets).

### Pushing updates
Run `bash ../build.sh`, then from this folder: `git add . && git commit -m "update"
&& git push`. Agents get the new version automatically via the Customize → Plugins
panel.

---

## What's in this folder
```
newcomer-ai-marketplace/
├── .claude-plugin/
│   └── marketplace.json          ← the catalog (lists the plugin)
├── newcomer-first-responder/     ← the plugin itself (v0.5.0)
└── PUBLISH.md                    ← this guide
```

## Tips
- Keep the repo **private** — this is your internal IP and your recruiting edge.
- Bump the plugin's version in `newcomer-first-responder/.claude-plugin/plugin.json`
  and the `version` in `marketplace.json` each release so agents see updates.
- Want it dead simple for non-technical agents? I can write a one-page "install in 2
  steps" sheet with screenshots to drop in the repo.
