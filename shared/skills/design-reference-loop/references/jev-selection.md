# Optional Jev concept selection — proposed boundary

**Status:** documentation plus an offline packet checker. No live Jev integration, registered tool, API request, receipt collector or background process is included.

Existing jev-layer `jev_route` selects capabilities (tools/skills/models/etc.). A design concept is not an executable capability: do not encode concepts as fake tools. A future separately reviewed adapter may use the decision provider's typed choice primitive and normalize it to this design-only proposal contract. `jev_select_candidate` is a possible future name, not an existing supported API.

## Ownership

1. The host builds a bounded brief and 3–5 concepts through its approved generator.
2. A human/host reviews mandatory constraints. `pass` requires a non-empty evidence note; `fail`, `unmeasured` or absent checks exclude a concept from advisory selection. These are supplied attestations, not independently verified facts; the checker is not a security boundary.
3. The local helper removes VS probabilities and check notes from the minimal outbound packet. Review the remaining goal/surface/summaries for privacy before any external call. Removing fields is not a complete secret detector.
4. An authorized adapter may ask Jev for a choice from exactly the supplied ids. Evaluate fit, clarity and feasibility as distinct criteria; a single choice cannot measure universal aesthetic quality.
5. Normalize the provider answer to the strict shape below. The host must reject unknown/stale/excluded ids. Jev's probability/confidence is not user approval or a guarantee of quality.
6. The user chooses the direction. The host implements and tests it. No returned text/id is executed as code, a command, a path or a tool name.

## Local contract

`examples/candidates.json` is the input contract example (paths relative to the design pack root). `brief.required_checks` is a non-empty list of unique ids. Each candidate check has `status` (`pass`, `fail`, `unmeasured`) and a short `evidence`. Input has two to five uniquely named concepts. Required fields and bounds are enforced by the stdlib helper; it is the executable contract, not a separate JSON Schema implementation.

Normalized design decision (not raw `jev_route` output):

```json
{
  "schema_version": 1,
  "request_id": "fixture-design-01",
  "status": "selected",
  "candidate_id": "editorial",
  "provider": "fixture"
}
```

The included decision uses `provider: fixture` because it is hand-authored synthetic test data. A future adapter must preserve provenance honestly. Do not label fixtures as real Jev results. Runtime correlation ids and host-local receipts should be mapped explicitly when that adapter is implemented; do not mutate the existing Jev receipt schema or publish replay.

## Failure behavior

Absent, malformed, unavailable or inconclusive advice returns to manual selection, without a guessed winner or a paid fallback. Empty eligible sets require revisiting the brief/constraints, not overriding them. One timed, bounded provider request would be the initial adapter design; provider retry semantics belong to the host and must be reviewed separately.

`execution.enabled` remains false even for a valid proposal. `requires_user_choice` remains true. This is a shortlist workflow, not an executor. The helper performs no network or permission changes.

Before any real connection: resolve the intended pinned Jev revision, inspect the selected runtime and existing MCP endpoints, confirm the data and cost boundary, add transport/timeout tests, and prove ordinary manual selection still works when Jev is off. Never silently replace a working Jev endpoint or add a second one.
