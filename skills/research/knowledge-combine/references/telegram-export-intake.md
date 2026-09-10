# Telegram HTML/ZIP export intake

## Safe inventory

1. Check ZIP validity, compressed/uncompressed size, and entry count before extraction.
2. Locate `messages.html`; parse message blocks with a local HTML parser.
3. Produce a local-only inventory: message count, date range, relevant candidate titles/themes. Do not add full exports, media, handles, or private text to vault/GitHub.

## Candidate selection

Select only material relevant to the stated target, for example:

- agent and harness workflow;
- local coding and handoffs;
- knowledge intake, vault, and source quality;
- learning-system patterns;
- proof-first Telegram/X content.

Exclude personal posts, ads/referrals, intimate/identifying information, and unrelated discussion. Promotional or anecdotal claims may be a pattern lead, never evidence by themselves.

## NotebookLM grounded-synthesis loop

1. Create a temporary local staging directory outside the vault.
2. Write a sanitized Markdown source pack with candidate labels, cleaned excerpts, and no handles/media.
3. Use the configured NotebookLM profile to create a notebook and upload **only** that sanitized pack.
4. Ask for a table containing each selected candidate, claim, KEEP/ADAPT/LATER/REJECT verdict, risk, and minimal safe next step.
5. Ask a second coverage question if the first answer skips any candidate.
6. Do not store NotebookLM raw output in the Git-backed vault unless the user explicitly asks; turn it into a concise curated note instead.

## Curated-note reminders

- Prefer **ADAPT**: carry over the engineering principle, not someone else’s skill/MCP/prompt/runtime.
- Keep security-sensitive recommendations conservative: external MCP, model routers, agent networks, and quick public deployment are normally REJECT for private contexts.
- Distinguish a pattern’s usefulness from the reliability of the post that mentioned it.
- Link the final note from both topic index and MOC.

## Completion gate

Before reporting: read note, scan changed note for secrets, run diff checks, commit and push unless `draft/no-push`, then report paths + commit hash + clean/dirty status.
