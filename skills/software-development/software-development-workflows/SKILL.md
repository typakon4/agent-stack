---
name: software-development-workflows
description: "Class-level software-development workflows: planning, spikes, TDD, debugging, code review, release recon, and debugger tooling."
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [software-development, planning, debugging, testing, code-review, tdd, spikes, release-recon]
---

# Software Development Workflows

Use this skill for general software engineering tasks where the user asks to plan, build, debug, test, review, validate a release, or coordinate implementation work. This is the umbrella for development process skills; load more specialized package/tool skills only when the task requires a specific external system.

## Workflow chooser

- **Planning / plan mode**: when the user asks for a plan, explicitly wants no code changes, or the next steps are ambiguous.
- **Spike**: when a risky technical assumption must be validated before committing to an implementation.
- **TDD**: when behavior is clear enough to encode as tests before implementation.
- **Systematic debugging**: when something is broken and root cause is unknown.
- **Code review / pre-commit review**: before shipping or when asked to audit a diff.
- **Release status recon**: when verifying whether a feature/app is real, runnable, released, or only announced.
- **Debugger tooling**: use Node `--inspect`/CDP for Node.js runtime state, and `pdb`/`debugpy` for Python runtime state.

## Planning and plan mode

When asked to plan, create a durable markdown plan under `.hermes/plans/` and do not edit production files unless the user explicitly switches to execution. A good plan has bite-sized tasks, file paths, expected test commands, risks, and verification gates. Prefer concrete checklists over broad milestones.

### Idea-to-build boundary

A user sharing a concept, architecture sketch, or content angle is not automatically approval to create a repository, service, bot, cron job, or external integration. Before implementation, identify the target surface and confirm the intended first artifact:

```text
idea / research note
→ local dry-run
→ existing-agent profile or separate service
→ separate messaging bot or existing chat/topic
→ scheduled automation
```

Do not infer an adjacent surface just because it seems technically attractive. A Telegram workflow may mean a dedicated Hermes profile/chat with cron jobs, not a new standalone Bot API service. If the user has not explicitly asked to build or selected the surface, return a scoped recommendation or plan and wait. Once they explicitly choose and ask to proceed, build the smallest reversible slice first; do not expand it into a larger product without another approval.

## Agent-infrastructure finish line

For agent/Codex/Hermes setup work, define a **v1 stop condition before expanding the toolchain**. A useful v1 is a small, exercised loop — e.g. baseline instructions, one approved intake gate, one real-project review, and one verified task. Do not keep adding skills, registries, plugins, or maintenance passes merely because they could help someday. Defer optional cleanup (memory refinement, ACL repair, duplicate-tool consolidation) to a maintenance backlog unless a current task is blocked by it.

## Spikes

Use a spike for unknown libraries, APIs, performance claims, parsing formats, or integration feasibility. Keep it throwaway, isolate it from production paths, record the exact command/output that answers the question, then either discard it or convert the proven approach into an implementation plan.

## Test-driven development

Follow RED-GREEN-REFACTOR: add or update a failing test first, run the narrow test to confirm the failure is meaningful, implement the smallest fix, rerun the narrow test, then run the relevant broader suite. Do not retrofit tests only after the code unless the user explicitly rejects TDD.

## Systematic debugging

Use four phases:
1. Reproduce the issue with the smallest command or input.
2. Observe with logs, traces, assertions, or debugger state.
3. Form and falsify hypotheses; avoid editing until the failure mode is understood.
4. Patch, then verify with the original repro and a regression test when possible.

## Code review / pre-commit review

Review security, correctness, data loss, concurrency, error handling, API compatibility, tests, and operational risk. Run local quality gates when available. If fixing findings, make minimal edits and rerun the affected gates. Report residual risk instead of claiming complete safety without evidence.

## Release status reconnaissance

Triangulate docs, release notes, repository tree, commits/tags, package versions, build scripts, binary artifacts, and runnable demos. Distinguish announced, merged, packaged, released, and operational states. Prefer live verification over marketing pages.

## Debugger tooling

### Node.js

For hard Node bugs, launch with `--inspect` or `--inspect-brk` and connect through Chrome DevTools Protocol rather than relying only on logs. Inspect breakpoints, scopes, promises, async stacks, and runtime expressions. Keep the debug process tracked and terminate it when done.

### Python

Use `pdb` for quick local stepping and `debugpy` when a DAP-style remote debugger is useful. Insert temporary breakpoints only in throwaway branches or remove them before finalizing. Verify fixes with tests, not debugger inspection alone.

## Specialized lanes absorbed here

- **Web-app dogfooding / exploratory QA**: when the user asks to test a web app, explore like a real user, capture screenshots/logs, classify issues, and produce a reproducible bug report.
- **Parallel simplification cleanup**: when recent code changes need a focused cleanup pass, review the working tree or requested diff for needless complexity, dead paths, naming drift, and test gaps; use subagents only when the scope justifies it.
- **Local agent-backed apps**: when an app should call an already-authenticated local Hermes/Codex/agent CLI as a backend instead of collecting model API keys inside the app, keep the agent boundary server-side and verify request/response parsing.

## Verification checklist

- The chosen workflow matches the task state (planning vs execution vs debugging vs review).
- The result is grounded in actual file reads, command output, tests, or live verification.
- Any production edit has an associated check or clear explanation of why a check could not run.
- Temporary spike/debug artifacts are removed or clearly named as disposable.
