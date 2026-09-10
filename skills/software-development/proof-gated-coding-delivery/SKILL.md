---
name: proof-gated-coding-delivery
description: "Deliver external coding-agent work through writable checkpoints, isolated runtime proof, approved-UI reconciliation, and evidence-based handoffs."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [codex, coding-agents, git, worktrees, verification, staging, ui-parity]
---

# Proof-Gated Coding Delivery

Use when Hermes coordinates an external coding agent on a non-trivial repository change and must reconcile a dirty worktree, exact approved UI, local runtime proof, or release readiness. This is a delivery discipline, not permission to deploy.

## Finish line

Report only the strongest state actually proved:

- **implementation candidate** — source changes exist and static checks may pass;
- **local staging-proven candidate** — isolated local runtime, core flows, and relevant authorization checks have evidence;
- **production-ready** — only after real provider, data, deployment, observability, policy, and release gates have explicit evidence.

Never label a demo payment, local file store, mock operation, or build-only success as a real-sale capability.

## Writable-checkpoint gate

Before stateful work (migrations, local database seed, containers), create a checkpoint in a writable repository.

### Sandbox Git metadata boundary

An agent sandbox can sometimes edit source files while being blocked from Git metadata such as `HEAD`, `index`, `objects`, refs, or reflogs. Treat that as a checkout ownership boundary.

1. Capture source branch, HEAD, status, `git diff --stat`, `git diff --check`, changed tracked files, and non-ignored untracked files.
2. Use only a narrow probe to establish the symptom. Do not progressively grant broad ACL access across `.git`; commits necessarily need several metadata paths.
3. Prefer a new agent-owned writable local clone/worktree. Keep the original dirty checkout read-only.
4. Transfer tracked changes with a binary-safe patch and untracked source with an explicit `git ls-files --others --exclude-standard` manifest.
5. Exclude ignored files, secrets, local env files, dependencies, caches, generated exports, and runtime volumes.
6. Compare changed tracked and intended untracked files with a hash manifest before staging.
7. Commit in the writable clone using the already configured user identity. Do not push unless explicitly approved.
8. Handoff must include clone path, branch, commit SHA, final status, and proof that the original checkout was unchanged.

## Isolated local runtime proof

Use runtime proof only after the checkpoint is clean and reproducible.

1. Read project local-development and Compose documentation first.
2. Use a distinct Compose project name and a new disposable database/volume.
3. Prove before migrations or seed that the target is local/container-only, not remote/shared/production, and contains no real data.
4. Bind local database ports to `127.0.0.1`, not all interfaces, unless a reviewed project requirement says otherwise.
5. Keep container runtime data on the owner-approved storage surface; do not silently fall back to another drive or location.
6. Use ephemeral local secrets and never print full connection strings or tokens.
7. Run migrations and reset-capable seed scripts only after the disposable-target proof.
8. Exercise a real minimum flow and its trust boundaries: health, auth, authoritative order/write path, state transition, cross-user access denial, and role checks relevant to the task.
9. Stop local services after proof unless the user asks to keep them running. Report whether volumes remain and why.

## Approved deployed UI reconciliation

When the user names a deployed page as approved, explicitly name the target surface — for example, root static landing, not mobile/API/operations — and use the deployment as the visual and interaction source of truth for that surface.

1. Inspect deployed HTML, loaded asset versions, CSS, required DOM hooks, and representative live interactions before editing local source.
2. Compare local HTML, CSS, and JavaScript as one compatible unit. A missing DOM hook can crash initialization before rendering or handler registration.
3. Restore coherent parity; do not merely suppress a null dereference while leaving a different layout or interaction contract.
4. Do not rewrite approved copy, redesign, or add unrelated behavior during a parity pass. Put legal/commercial copy review in a separately approved batch.
5. Test controls on the approved deployment when possible. If a control is inert there too, record it as an approved-baseline limitation rather than creating unrequested local divergence.
6. Keep unrelated product surfaces out of the diff. If local browser policy blocks screenshots, report pixel parity as unproven; do not claim it.

See `references/windows-sandbox-and-ui-parity.md` for compact clone-transfer, loopback Compose, and approved-UI evidence checklists.

## Goal-run discipline and cross-platform delivery

External coding-agent `/goal` runs should be bounded around a stakeholder-visible vertical slice, not an abstract backlog. Define the visible proof before starting:

```text
customer action → persisted server state → staff action → customer sees updated state
```

- Set a timebox and terminal state: required gates, one direct correction at most, clean worktree, commit, final handoff; no push or deployment unless separately authorized.
- A status update or intermediate commit is **not** a final handoff. Do not deploy from it.
- If the agent drifts into recursive auditing, require it to finish one highest-value unverified lifecycle, document remaining uncertainty, and stop rather than widening scope.
- Before accepting a final report, obtain the final commit SHA, `git status --short`, `git diff --check`, exact passed/failed checks, and an explicit list of runtime paths not rerun after any data/schema correction.

For cross-platform products, prove the boundaries separately:

1. **Marketing/discovery landing** — CTA reaches the real customer app rather than a static mock.
2. **Shared customer app** — the same API-backed path works in the mobile codebase and its web export; language/market choices persist as designed.
3. **Backend/data** — fresh isolated database/volume, migrations, seed, authoritative totals/state, and trust-boundary denials.
4. **Staff operations** — a protected seller/admin action changes the same persisted order that the customer can refresh and observe.

For seller-created inventory or any actor-authored listing, the staff proof must use a **new listing created during the run**: create → attach media → publish → public catalog discovers the same record → buyer orders it. A seeded product plus a separate seller order does not prove this business loop.

When a reported UI error follows a successful write, query the persisted record before calling it data loss. In async React form handlers, capture the form element before the first `await` (for example, `const formElement = event.currentTarget`) and reset that local reference after the request; `event.currentTarget` can be null by then. Regression proof must show create → returned UI list/reload contains that record.

Time-sensitive fixtures are a release gate: before calling a demo live, assert that public catalog fixtures have a future availability deadline. Expired seed inventory can make a technically healthy marketplace look empty; refresh disposable demo fixtures deliberately and report the data refresh separately from source changes.

If an old local database has incompatible encoding, migrations, or fixture state, do not classify the flow as runtime-proven from a stale browser session. Re-run the complete buyer → staff → buyer lifecycle on a fresh UTF-8 isolated database before promotion.

Use an explicit release matrix:

```text
Visible stakeholder demo: yes/no
Closed pilot: yes/no
Public launch: yes/no
Real payment/regulated capability: yes/no
Evidence still missing: ...
```

## Evidence handoff

Use this compact final structure:

```markdown
# Delivery Handoff

## Checkpoint
## Source / approved UI evidence
## Files changed
## Commands and actual results
## Runtime and authorization evidence
## Visual evidence or blocker
## Git status / commits
## Remaining blockers and owner decisions
## Release classification
```

## Pitfalls

- A passing test suite from a different checkout is baseline evidence, not proof of the current dirty integration.
- `npm audit` findings must be classified; never use `npm audit fix` as an unreviewed release step.
- A public deployment may be visually authoritative while its content/claims still need separate legal or commercial review.
- Do not let a local browser-policy blocker become an excuse to fabricate screenshot or pixel-parity evidence.
- Do not let production readiness collapse into an endless agent loop: after the bounded proof and handoff, stop and request the next explicit provider, policy, or deployment approval.
