# Portable agent contour (repository name retained)

This existing Git repository is the **one** source for reviewed, user-owned, secret-free behavior shared selectively between VPS Hermes and PC Hermes. It is not a copy of either runtime, a config manager, or a state-sync service. Keep its history; do not rename it just for aesthetics. `manifest.yaml` names eligible components and targets. Nothing is installed automatically.

## Boundaries

- **VPS Hermes:** always-on gateway, Telegram, scheduled/background work and server integrations. Its current default profile owns the production Telegram token.
- **PC Hermes:** interactive GUI/TUI, local files/models, browser, content/media and experiments. Start with one default profile. No VPS Telegram token.
- **PC OMP:** existing optimized coding runtime. Preserve Graphify/CodeGraph/ripgrep, Ponytail/full, i-have-adhd, diff-shrink, LSP, specialized subagents, Jev stdio MCP and RTK Pi-compatible tooling. This repository must not replace its runtime configuration or add a second Jev integration.

`SOUL.md` and `personal-operator-baseline` are for Hermes, **not** replacement OMP instructions. Cross-runtime skills can be added only after reviewing actual tool mappings; don't duplicate full SKILL.md logic for names alone. The listed media skills are initially PC-only. `multi-host-agent-operations` is on hold: parts assume central shared memory and older Windows paths, neither of which is a target requirement. See `SKILLS-MANIFEST.md` for the blocked research skill.

Never sync live databases, WAL/SHM, sessions, Telegram/cron receipts, browser data, Jev replay files, OAuth/auth stores or caches between hosts. Move selected knowledge only as reviewed Markdown/YAML/JSON. Store provider keys, bot tokens, webhook secrets and machine-specific endpoints in each profile's local secret store. `config.safe-defaults.yaml` is an **example for manual review**, not a config overlay: its memory-approval and delegation values differ from the VPS live config.

This repo must contain no `.env`, `auth.json`, credentials, private keys, browser cookies, live session data, state databases, Jev replay JSONL, logs, generated dependencies or machine-specific absolute paths. Scan new skills and review the **report-level** verdict before marking them `reviewed`; a LOW/SAFE verdict is not proof that instructions fit both runtimes. Re-check content and target compatibility after edits.

OMP's file-prefetch can include the first ~100 lines of up to four explicitly referenced files. Path redaction **does not redact secrets inside those files**: never point it at `.env`, auth, keys or credential stores without explicit approval. Keep `~/.omp/agent/mcp.json`, `jev-config.json`, LSP paths, model roles, extensions, subagents, UI, credentials and replay local. Jev remains advisory through the existing six MCP tools: no automatic model/thinking changes or context deletion; do not reintroduce direct TypeSafe, alternate compaction or a duplicate Jev extension.

## Review and apply

1. Pull/review a contour commit and `manifest.yaml`; do not auto-pull into production.
2. Select one component and target profile explicitly. `hold` entries cannot be installed; `optional` entries require a named use case. Prefer a manual diff for `SOUL.md`, config examples and templates.
3. Back up the **target** before replacing any skill, then install only the selected skill; never overwrite all of `~/.hermes`, `~/.omp`, or an upstream checkout. The optional `apply.py` supports skill-only dry-run and explicit application.
4. Start a fresh session and exercise the selected skill. Check OMP/other host separately only if that host was targeted.

`handoffs/ACTIVE.md` is a non-secret template, not a live synchronized session. The official Hermes updater owns Hermes code; this repository owns only selected user behavior. KISA Stack inspired the small skill-install idea; its plugins/policies are **not** an installation checklist (RTK is already intentionally present in OMP).
