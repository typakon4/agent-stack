# Two Hermes nodes + existing OMP — installation and maintenance notes

These are future steps, not actions performed by this repository. VPS Hermes remains online. Do not install PC Hermes or change production VPS services as a side effect of applying a skill.

## PC Hermes bootstrap (not performed)

1. On the present Windows workstation, prefer the **official signed Windows Desktop bundle** with its native Hermes agent/GUI; check its current platform instructions before installation. If the target PC later runs Linux/Omarchy, use the supported Linux source install and native Hermes Desktop/TUI instead. Do not transplant Windows executables, shellPath, LSP paths, or `%LOCALAPPDATA%` paths to Linux. Windows source-install data is `%LOCALAPPDATA%\\hermes`; a bundled Desktop installation uses its documented platform data directory. Resolve the actual Hermes home *after* installing, not by copying the VPS path.
2. Configure one default PC profile and authenticate models **locally**. Keep its own sessions, state, memory, browser data and credentials. Leave the production Telegram token on the VPS; no second poller or local gateway until there is a named use case. Configure browser, local models and media dependencies only as needed. Use native GUI/TUI, not a custom app.
3. Review `manifest.yaml`; try `apply.py --target PC_HERMES --skills-dir <actual-absolute-skills-dir> --skill <reviewed-name>` without `--apply` first. The helper never installs SOUL or config: review/merge SOUL manually and ignore example config values that conflict with local defaults. Optional skills need a concrete task. Do not copy VPS databases, venv, systemd units, Caddy, provider secrets or replay JSONL.
4. Exercise a real local session in Desktop/TUI, the chosen tools and one selected skill. Verify the PC workdir/files remain local. A separately configured remote VPS connection is optional; it is not the PC's local state or a reason to duplicate Telegram ownership.
5. Preserve OMP as its own coding runtime. Never replace `~/.omp/agent/mcp.json`, model roles, LSP paths, local subagents, extensions, replay, provider credentials or existing Jev stdio MCP from this repository. A cross-runtime skill may target OMP only after reviewing actual tools and adding an explicit OMP target to the manifest.

Official references: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/getting-started/installation.md and https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/desktop.md.

## Functional Study / Content / Research boundaries

| Context | Start with | Separate profile only if |
|---|---|---|
| Study | `ai-engineering-tutor` skill, native sessions/memory, selected learning plans and quizzes; remote use can stay in the VPS default profile | Durable study history, instructions, model/provider or schedules must be isolated from server/Telegram conversations |
| Content | Background evidence/draft workflows on VPS; interactive media and artifacts on PC with optional creative skills | Publishing credentials, editorial policy or persistent inbox/state require a different trust boundary. No automatic publishing |
| Research | `knowledge-combine` and native research/delegation; scheduled research on VPS if needed | Separate secrets, permissions, budget or long-running state justify isolation. Blocked `research-knowledge-workflows` must not be enabled unchanged |

Do not pre-create `study`, `content`, `research`, `bot` or `experimental` profiles. A profile is for meaningful isolation, not a menu item. A skill/workflow covers the currently proven requirement.

## Independent updates and rollback

Track four versions independently: VPS/PC Hermes upstream commits, contour Git commit, Jev commit for each node, and OMP runtime version. VPS and PC need compatible contracts, not identical Hermes hashes. Never modify Hermes upstream files or auto-pull this contour into production.

1. Read release notes and relevant schema/adapter changes; back up the target node with native WAL-safe snapshot and prove restore on an isolated copy. Check the target profile's actual SQLite/Python versions, not the OS Python's older SQLite.
2. Test a proposed Hermes update on PC or an isolated profile first: new session, critical skills, gateway/MCP, Jev six tool names, browser only if used. Do not repeat paid OpenRouter tests without a reason and approval.
3. Review the contour diff and scan any modified skills; use an explicit manifest target, dry-run and backup-before-replace. Test one behavior on each targeted host; OMP remains unchanged unless a real defect is demonstrated.
4. VPS maintenance requires separate approval for service restarts, runtime switches and schema migrations. After an approved update, verify the live launcher/commit, Telegram single-token ownership, scheduled jobs and state schema. Retain old service definitions and a compatible backup.
5. Git rollback alone is not a DB rollback. If schema changed, stop and plan an approved offline restore with all writers stopped; never replace `state.db` or delete WAL while a gateway/dashboard/serve holds it.
