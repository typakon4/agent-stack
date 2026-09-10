# Knowledge and context architecture

Use this decision order when a user asks for RAG, a local brain, or more agent context across hosts.

## Start with the smallest layer that solves the retrieval problem

| Need | First choice | Boundary |
|---|---|---|
| Stable preferences, operating rules, compact environment facts | Hermes built-in memory + `SOUL.md` + reviewed skills | Per Hermes home/profile; do not share its files between hosts. |
| Recover facts from prior local chats | `session_search` | Host-local session corpus; not a document knowledge base. |
| Search durable Markdown notes and handoffs | Git-backed vault with stable names, links, and explicit source references | Share the repository, never the agent home. |
| Semantic continuity between laptop and VPS agents | One external Hermes memory provider, preferably private/self-hosted where appropriate | Configure each host separately; use one named bank and verify retain/recall from both hosts. Hermes allows only one external memory provider active at a time. |
| Retrieval over a large corpus of documents, repositories, PDFs, and notes with citations | A dedicated knowledge brain/RAG service exposed through MCP or a narrow CLI | This is a separate system with ingestion, embeddings, index lifecycle, access control, and observability. |

## Separate agent memory from document RAG

Do not install a knowledge brain merely to make the agent remember user preferences. A large RAG service adds indexing and maintenance cost, while built-in or external memory already handles compact, evolving user context.

Use a document-RAG system only after defining:

1. the corpus roots and which sources are private;
2. the retrieval question it must answer better than file search or the vault;
3. ingestion/update cadence and deletion behavior;
4. embedding/model cost or local hardware budget;
5. citations/provenance in answers;
6. MCP/CLI permissions and whether the agent may write to the corpus.

## GBrain-style systems

Treat GBrain-style software as an opinionated, standalone Markdown-first brain rather than a drop-in Hermes-memory toggle. It can be a fit for a personal vault spanning documents and repositories, but it overlaps with a Git-backed vault and requires an explicit source-of-truth and write policy.

Before connecting it to Hermes:

- inspect and security-scan the exact revision and integration surface;
- keep the knowledge corpus separate from credentials, raw browser data, and agent sessions;
- begin read-only through a narrow MCP tool selection or CLI probe;
- test retrieval against known documents and require source paths/citations before relying on it;
- keep service access private over Tailscale when it runs off-device.

## Rollout sequence

1. Establish the secret-free portable baseline and curated skills.
2. Use the Markdown vault plus normal file/session search for real work.
3. Add shared external memory only when both hosts need the same semantic continuity.
4. Add dedicated RAG only when measured retrieval gaps remain; validate a small corpus before indexing the whole vault.
