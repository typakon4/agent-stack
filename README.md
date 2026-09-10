# Hermes portable baseline

A secret-free, Git-backed operating baseline for a new Hermes installation.

## Included

- `SOUL.md` — concise response behavior.
- `skills/personal-operator-baseline/` — reusable work rules for development, learning, creative rendering, and external actions.
- `config.safe-defaults.yaml` — intentionally conservative defaults; it contains no provider, API, OAuth, Telegram, browser, MCP, or memory connection settings.
- `handoffs/ACTIVE.md` — a durable project handoff template.
- `SKILLS-MANIFEST.md` — the reviewed queue for the next skill-transfer batch.

## Intentionally excluded

- `.env`, `auth.json`, provider keys, Telegram tokens, browser profiles/cookies, SSH/Git credentials.
- Raw sessions, local memory databases, logs, cron jobs, gateway/service units, machine paths.
- Full `config.yaml`; merge safe settings manually instead of overwriting the target host.

## Install on the Omarchy machine

1. Install Hermes and run `hermes setup` / `hermes login` **on that machine**.
2. Clone this repository, then review it:
   ```bash
   git clone <your-repo-url> ~/Projects/hermes-portable-baseline
   cd ~/Projects/hermes-portable-baseline
   ```
3. Copy the baseline files into the active default profile:
   ```bash
   cp SOUL.md ~/.hermes/SOUL.md
   mkdir -p ~/.hermes/skills
   cp -a skills/. ~/.hermes/skills/
   ```
   For a named profile, replace `~/.hermes` with `~/.hermes/profiles/<profile>`.
4. Merge only the reviewed keys from `config.safe-defaults.yaml` into the target `config.yaml`; do not replace the whole file.
5. Start a fresh session, then verify:
   ```bash
   hermes skills list
   hermes doctor
   ```

Run the skill scan again after each change before propagating the skill:
```bash
~/.hermes/scripts/skillspector-scan skills/personal-operator-baseline --format json --output audits/personal-operator-baseline.json
```

## Updating

Commit baseline changes here. Each machine pulls the repository and repeats the review/copy steps. Keep credentials and host-local integrations separate.
