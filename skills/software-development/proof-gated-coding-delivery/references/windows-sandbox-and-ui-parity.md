# Windows Sandbox Git + Approved UI Reference

Use this as a concise proof checklist when an external coding agent works in a Windows checkout but must preserve a user-owned original worktree.

## Writable clone transfer checklist

1. In the original checkout, record `git status --short --untracked-files=all`, `git diff --stat`, `git diff --check`, changed tracked files, and non-ignored untracked files.
2. Clone locally into a sandbox-owned writable destination.
3. Apply a binary-safe tracked diff.
4. Transfer only files listed by `git ls-files --others --exclude-standard`.
5. Hash each intended source file before/after transfer; exclude ignored env files, dependencies, exports, and runtime data.
6. Commit only in the clone. Preserve original checkout status as a proof artifact.

## Local container proof checklist

- Assign a distinct Compose project name.
- Change database host publishing from a broad host mapping to explicit loopback binding, e.g. `127.0.0.1:<host-port>:<container-port>`.
- Verify `docker compose config`, container labels, host port, named-volume ownership, and database readiness before migrations.
- Run migration/seed only against a new disposable local database.
- Exercise a write flow plus authorization-denial paths; cleanly stop services after evidence collection.

## Approved deployed UI parity checklist

- Record approved URL, inspection time, loaded script/style asset names, and a few representative interactions.
- Build a DOM-hook matrix: each selector required by local initialization must exist in the matching local rendered state.
- Treat a remote working interaction as a contract; treat a remote inert control as a documented baseline limitation unless separately approved.
- If direct remote asset retrieval or local screenshots are blocked, report the exact limitation and keep claims limited to inspected DOM/behavior/static evidence.
