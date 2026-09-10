---
name: knowledge-combine
description: Turn external source collections into safe, curated, Git-backed vault knowledge using bounded synthesis and explicit verdicts.
---

# Knowledge Combine

Use when the user sends articles, channel exports, folders, source packs, transcripts, or multiple links and asks to "перемолоть", synthesize, extract patterns, or improve their workflows/learning system.

## Operating principle

The combine is a **filter**, not another firehose:

```text
inputs → inventory → bounded/sanitized source pack → grounded synthesis
→ verdicts → curated note → index/MOC → verify → commit/push
```

Route results by meaning, not by chat:

- Hermes, agents, NotebookLM, vault systems, local coding workflows → `topics/hermes-workflows/`
- learning curriculum / Python / AI engineering → `topics/ai-engineering/`
- career / relocation → `topics/career-relocation/`

## Source privacy boundary

Treat supplied collections as private by default.

Never commit raw archives, full exports, media, personal conversations, handles, account data, referral codes, or unrelated material. Build a small **sanitized local source pack** containing only relevant excerpts/paraphrases and enough provenance to ground synthesis.

When source material is long, multi-item, or explicitly called a Knowledge Combine, prefer NotebookLM-first using the configured grounded-synthesis profile. For Telegram exports, upload the sanitized pack—not the raw source collection. For YouTube batches, add the URLs directly as sources when supported. If NotebookLM is bypassed, state why in the final report.

## Verdict rubric

Assign every finding exactly one verdict:

- **KEEP** — safe and compatible pattern with immediate value.
- **ADAPT** — useful principle; reproduce locally with explicit boundaries rather than copying foreign prompts, skills, MCPs, or runtime.
- **LATER** — plausible but needs a demonstrated gap, primary-source review, or isolated proof of concept.
- **REJECT** — unacceptable privacy/trust/publication risk or no meaningful fit.

Default safety bias:

- public remote MCPs, unofficial model routers, agent networks, and accidental public deployments → **REJECT** for private workspaces;
- host migrations, heavy local RAG, and whole-site cloning → normally **LATER**;
- bounded source cleanup, acceptance criteria, review-only audits, and proof-first content patterns → often **KEEP** or **ADAPT**.

## Curation requirements

A curated note must include:

1. scope and source-handling boundary;
2. executive signal: reusable principles, not a tool dump;
3. findings table with verdict, risk/boundary, and minimal safe next step;
4. explicit anti-patterns / what not to copy;
5. three strongest safe improvements;
6. provenance and limitations, especially promotions, anecdotes, or unverified benchmark claims.

Update the relevant topic index and MOC to avoid orphan notes.

## Verification and publication

Before finalizing:

1. Read the curated note back.
2. Check new wikilinks and changed paths.
3. Scan changed content for secrets/token/key/private-key patterns.
4. Inspect diff and whitespace.
5. Commit + push by default unless the user explicitly says `draft` or `no-push`.

Final Telegram report: Russian paths, strongest findings, what was intentionally excluded, commit hash, clean/dirty Git status, and three safe next proposals. Curated vault notes should be Russian; retain English technical identifiers only when they aid findability.

## References

- `references/telegram-export-intake.md` — safe pipeline for Telegram HTML/ZIP channel exports and NotebookLM coverage checks.
- `references/telegram-youtube-combine.md` — combined Telegram ZIP and YouTube intake, NotebookLM prompts, source boundaries, and Hermes-specific reality checks.
