# NotebookLM Research Layer for AI Engineering Learning

Use this reference when the user wants to connect Google NotebookLM with the existing `rei-vault/topics/ai-engineering` learning system.

## Core pattern

NotebookLM is useful, but it is not connected to the Obsidian/git vault by itself. Treat it as a source-based reading assistant, not as the source of truth.

Recommended roles:

```text
Obsidian/git = source of truth
Hermes       = tutor, planner, anti-chaos filter, progress/checkpoint
NotebookLM   = source-based reading assistant / large-material Q&A
Codex        = repo editing, markdown note generation, backlog updates
Zed          = editor for writing Python by hand
```

## Required setup for a NotebookLM notebook

Before adding courses/articles/PDFs, create and upload a compact vault context source first.

Suggested file in the vault:

```text
topics/ai-engineering/research/notebooklm-vault-context-pack.md
```

This context pack should include:

- learner profile and current level;
- current focus, e.g. `Week 1 → Python basics → code by hand`;
- completed/current/next days;
- 30-day roadmap;
- long-term roadmap;
- folder map for `topics/ai-engineering/`;
- anti-chaos rules;
- `now / soon / later / reference / skip` classification rules;
- instructions that NotebookLM must not replace the vault roadmap.

Upload order:

```text
1. notebooklm-vault-context-pack.md
2. source pack / list of learning materials
3. external courses, docs, PDFs, videos, etc.
```

## Workflow

1. User adds materials to NotebookLM.
2. User asks NotebookLM to analyze the material against the vault context.
3. User saves or syncs the NotebookLM output into the repo, usually under:

```text
topics/ai-engineering/research/notebooklm-answer.md
```

4. Hermes reads the raw answer and creates a curated note, e.g.:

```text
topics/ai-engineering/research/notebooklm-python-month-1-triage.md
```

5. Hermes updates index/README links and, if useful, links only the current relevant part into the daily practice README.

## Curation rule

Raw NotebookLM output should not become the daily plan directly. Always triage it:

```text
raw NotebookLM answer → curated triage note → daily/self-study update if appropriate
```

For beginner Python, move topics like dictionaries, JSON, `try/except`, `requests`, OOP, decorators, Flask/Django, SQLAlchemy, bots, and advanced architecture to `soon`, `later`, or `reference` unless they match the current day/week.

Example from Day 05 lists:

- keep: `list`, `.append()`, `while` input loop, `for` over list, simple function receiving a list;
- postpone: dictionaries, JSON, `try/except`, calculator with error handling, web frameworks.

## NotebookLM prompt template

```text
Используй Vault Context Pack как источник правил и структуры.

Я сейчас на Week 1–4 Python-first AI engineering path.
Проанализируй загруженный материал и не ломай текущий roadmap.

Ответь:
1. Что это за материал?
2. Подходит ли он сейчас?
3. Статус: now / soon / later / reference / skip.
4. Почему?
5. Какие prerequisites?
6. Что можно забрать в практику на текущем этапе?
7. Что игнорировать пока?
8. Дай 3–5 маленьких заданий, если материал подходит.
9. Дай короткий markdown-блок для Obsidian.
```

## Pitfalls

- Do not make NotebookLM a second roadmap.
- Do not feed it only external courses; without the context pack it will not know the user's structure or current constraints.
- Do not treat a thousand-line answer as an action plan. Summarize, classify, and route only the relevant slice into daily practice.
- Keep source packs and raw answers under `research/`; keep daily coding under `projects/week-1-python-practice/`.
- Preserve the anti-copy-paste rule: NotebookLM may suggest drills, but the user still writes/fixes code by hand.
