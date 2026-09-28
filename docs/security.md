# Security boundaries

This repo is reviewed portable **behavior**, not live state. Do not commit `.env` files, auth/OAuth stores, provider keys, private keys, Telegram tokens, browser cookies/profiles, chat exports, schedules, logs, DB/WAL/SHM, Jev replay/JSONL/receipts, caches, private vault contents, or machine-specific config. Ignore patterns are defense in depth, not permission to add private data. Review every proposed skill and staged diff for secrets, hardcoded personal paths, unapproved network uploads, and implicit publication.

`tests/test_no_secrets.py` checks obvious file names and credential signatures in commit candidates and Git history. It cannot guarantee that all secrets have been found; human review is still required.

Keep credentials, model/provider settings, MCP registration, profile identity, sessions, and replay on the specific host. VPS and PC profiles are distinct; do not duplicate a production Telegram poller/token. OMP and Codex retain their own rules and MCP configs. Jev is pinned as external metadata only; a working OMP Jev MCP must not be replaced or duplicated. If a tool can publish, push, buy, send, delete, or deploy, require explicit target/action approval; the presence of credentials is not consent.

Treat source collections as private by default. Curate sanitized excerpts only after deciding whether a configured external synthesis service may receive them. Handoffs must contain reviewed facts and verification, not raw conversations or active session state. If a dry-run shows an unexpected destination or file, stop rather than applying.
