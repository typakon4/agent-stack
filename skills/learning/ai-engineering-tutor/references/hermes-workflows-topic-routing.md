# Hermes Workflows Topic Routing

Use this reference when workflow/research-system ideas appear while working on the user's AI engineering vault.

## Why this exists

The user wants one git-synced Obsidian vault to serve multiple chats/sessions, but without mixing active Python learning with meta-workflows about Hermes, NotebookLM, ChatGPT Pro, Codex, Google Drive, browser automation, or a future PC/laptop agent.

## Routing rule

```text
topics/ai-engineering/   = what the user is learning/practicing
topics/hermes-workflows/ = how the agent/research/knowledge system works
topics/reiops/           = future business/product layer, only if it grows enough
```

When a source/post is about learning Python or AI engineering materials, put it under `topics/ai-engineering/research/` and triage it against the current roadmap.

When a source/post is about tooling workflows — Hermes + NotebookLM, ChatGPT Pro deep research, Google Drive inbox, Obsidian automation, Smart Connections, Zettelkasten/MOC, local PC agents, browser/account setup — put it under `topics/hermes-workflows/`.

## Preferred structure

Use one vault/repo with topic folders rather than a separate repo per idea. This avoids multiple sources of truth while allowing cross-chat reuse.

Minimal shared structure:

```text
topics/
├── index.md
├── ai-engineering/
└── hermes-workflows/
    ├── index.md
    ├── inbox.md
    ├── architecture.md
    ├── research-pipelines/
    ├── notebooklm/
    ├── chatgpt-pro/
    ├── pc-agent/
    ├── templates/
    └── references/
```

## Intake pipeline

For workflow ideas copied from Reddit/X/Telegram/blogs:

1. Save the raw idea or a concise triage note under `topics/hermes-workflows/inbox.md` or `topics/hermes-workflows/references/`.
2. Classify: `now / soon / later / reference / skip`.
3. Extract the reusable pattern, not the hype.
4. Do not let workflow-system ideas mutate the active AI-learning roadmap unless they directly help the current Python-first path.
5. Only create automation/skills after the manual pipeline repeats and proves useful.

## Specific stance from the NotebookLM/Obsidian posts

Useful now:

- Hermes as active coordinator/triage layer.
- NotebookLM as bounded-source synthesis/audio/FAQ layer.
- ChatGPT Pro as optional long deep-research engine.
- Obsidian/git as source of truth.
- Source packs, raw output, curated triage.
- A future Google Drive inbox or PC agent as transport/automation layer.

Avoid for now:

- Full Zettelkasten atomization of every note.
- Graph-view/Smart Connections as the main learning mechanism.
- MCP/plugin-heavy setup as a prerequisite for Python learning.
- Treating NotebookLM or ChatGPT Pro output as a plan without Hermes/Obsidian triage.

## Response pattern

When the user brings a workflow-system post while learning:

```text
1. Briefly identify the pattern.
2. Say what is useful now vs later.
3. Route it to `topics/hermes-workflows/` if it is meta-workflow content.
4. Preserve `topics/ai-engineering/` for actual learning/practice.
```
