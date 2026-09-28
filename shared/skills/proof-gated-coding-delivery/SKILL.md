---
name: proof-gated-coding-delivery
description: Deliver coding-agent work through writable checkpoints, isolated runtime proof, approved-UI reconciliation, and evidence-based handoffs.
---

# Proof-gated coding delivery

Use when coordinating non-trivial repository changes or reconciling a dirty checkout, approved UI, local runtime proof, or release readiness. This discipline grants no permission to deploy, publish, commit, or push without authorization.

## Claim only the state proved

- **Implementation candidate:** source changes exist; static checks may pass.
- **Local staging-proven candidate:** a disposable local runtime and relevant core/authorization flows were actually exercised.
- **Production-ready:** real provider, data, policy, observability, deployment, and release gates have explicit evidence.

Do not label a demo payment, mock operation, local file store, or build-only success as real production capability.

## Writable checkpoint

Before migrations, seeds, or container state, identify a writable repository and capture the branch, HEAD, status, changed tracked files, and non-ignored untracked files. If a sandbox can edit source but not Git metadata, do not broaden `.git` permissions to force a commit. Prefer a separate writable local clone/worktree; preserve the original dirty checkout. Transfer tracked changes with a binary-safe patch and untracked source from an explicit file list, excluding ignored files, secrets, dependencies, generated exports, and runtime data. Compare intended file hashes before staging. Commit only if authorized; never push implicitly. Report checkout path, branch, final status, and whether the original checkout changed.

## Isolated local proof

Read project setup instructions. Use a distinct project name and disposable local data/volume. Before migrations or reset-capable seeds, prove the target is local and contains no real/shared data; bind published database ports to loopback unless the project explicitly requires otherwise. Use temporary secrets without printing them. Run the task's real minimum flow and trust boundaries (for example, write → persisted read, cross-user denial, and relevant roles); avoid counting a browser render as proof of a backend transition. Stop local services after proof unless requested otherwise; report remaining volumes. If data or schema changes after a test, rerun the affected flow before claiming it proved.

## Approved UI and cross-platform scope

When a user names a deployed page as approved, identify the exact surface. Compare live HTML, styles, loaded assets, DOM hooks, and representative interactions against local rendering. Restore coherent layout and behavior rather than hiding a null exception. Do not redesign approved copy or expand into unrelated surfaces. If screenshots or live controls cannot be inspected, name that evidence gap. For cross-platform features, prove each applicable customer UI, persisted API state, and authorized staff action against the same record; seeded records do not prove creation workflows.

## Bounded handoff

Define a stakeholder-visible flow and required evidence before starting an external agent run. An intermediate commit or status update is not the final handoff. Record exact checks/results on the final checkout, runtime and denial evidence, visual evidence or blocker, final Git status, remaining decisions, and the strongest release classification actually proved. Do not claim a check from another checkout or before a corrective edit as current evidence. No push, deployment, or production mutation without separate approval.
