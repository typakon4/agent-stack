# Deep Research → Practice-First Course Curation

Use when the learner supplies a broad external Deep Research report about courses, tools, AI engineering, or learning methods.

## Preserve the source, then curate

1. Save the report verbatim under the vault's research/raw area.
2. Create a separate curated triage note; never paste raw research directly into the operational roadmap.
3. Mark each recommendation `now`, `soon`, `later`, `reference`, or `skip`.
4. Preserve official source URLs and uncertainty; Deep Research citations are leads, not automatic proof.

## Default curation rule for this learner

Prefer this progression:

```text
Python/data handling
→ CLI project
→ modules/errors/tests
→ HTTP/API
→ one raw LLM SDK
→ tiny AI tool
```

Defer agents, RAG, LangGraph/LangChain-heavy projects, fine-tuning, local serving, Docker/Kubernetes, and new language tracks until the Python/API bridge is working.

## Compress calendar promises

If research proposes an 8-week plan but the available calendar is shorter or uncertain:

- turn it into a 6-week core plus optional polish;
- cut optional scope before adding catch-up debt;
- use session-based progression rather than strict day dates.

## Resource stack should stay small

For one phase, use at most:

- 1 core reference;
- 1 practice companion;
- 1 targeted official reference.

A resource must create a better explanation, exercise, artifact, review, or study workflow. Otherwise defer/skip it.

## NotebookLM handling

Treat NotebookLM as a recall/synthesis layer, never the source of truth:

```text
Obsidian/Git = canonical notes and code
NotebookLM = quizzes, flashcards, audio/video recap from a small curated packet
```

Use video for processes/pipelines; use quizzes/flashcards for syntax, definitions, and edge cases. Do not upload secrets, `.env` files, tokens, private logs, or raw credentials.

## Research cadence

Do not let research replace practice:

```text
four practical sessions → one 60–90 min research/curation session
```

A research session must produce one concrete artifact: a material note, curated resource, self-study drill, plugin decision, or workflow update.

## Learning session templates

Default:

```text
5 min recall
10 min one example/self-explanation
25 min hand-written build
15 min run/debug/verify
5 min log
```

Fallback:

```text
3 min recall → 17 min one micro-task → 7 min verify → 3 min log
```

## Provider choice for first LLM app

Do not configure a provider merely because a report recommends it. Before implementation explicitly decide:

- budget;
- privacy/data boundary;
- available account;
- structured-output needs.

Use exactly one provider's official Python quickstart for the first app.