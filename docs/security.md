# Security boundaries

This repo is reviewed portable **behavior**, not live state. Do not commit `.env` files, auth/OAuth stores, provider keys, private keys, Telegram tokens, browser cookies/profiles, chat exports, schedules, logs, DB/WAL/SHM, Jev replay/JSONL/receipts, caches, private vault contents, or machine-specific config. Ignore patterns are defense in depth, not permission to add private data. Review every proposed skill and staged diff for secrets, hardcoded personal paths, unapproved network uploads, and implicit publication.

`installers/safety.py` supplies the obvious filename/content checks used by both the installer and `tests/test_no_secrets.py`. The repository gate scans commit candidates and Git history; the installer scans selected sources before writing, including ordinary Markdown files. Matched credential values are never printed. These checks cannot guarantee that all secrets have been found; human review is still required.

Destination checks reject symlinks/junctions before resolving the path, then compare canonical paths against the repository. This also refuses Windows 8.3 aliases that refer to the repository or its ancestors/descendants. `--no-clobber` additionally refuses existing selected targets; intentional replacement without it preserves a backup.

Keep credentials, model/provider settings, MCP registration, profile identity, sessions, and replay on the specific host. VPS and PC profiles are distinct; do not duplicate a production Telegram poller/token. OMP and Codex retain their own rules and MCP configs. Jev is pinned as external metadata only; a working OMP Jev MCP must not be replaced or duplicated. If a tool can publish, push, buy, send, delete, or deploy, require explicit target/action approval; the presence of credentials is not consent.

Treat source collections as private by default. Curate sanitized excerpts only after deciding whether a configured external synthesis service may receive them. Handoffs must contain reviewed facts and verification, not raw conversations or active session state. If a dry-run shows an unexpected destination or file, stop rather than applying.
