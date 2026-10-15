# Evidence for a working design slice

Define task-specific pass/fail conditions before editing. Use the project's test commands and supported browsers; do not install a browser framework or start services without checking scope.

## Visual review

- Capture the actual changed local surface at an agreed desktop and mobile viewport. State measured sizes, not an invented device test.
- Check hierarchy, spacing, alignment, text wrapping, overflow, readability and states.
- Verify contrast and focus behavior with available tools; say when values are unmeasured.
- Inspect meaningful transitions and reduced-motion behavior if the task includes animation.
- Compare with the approved baseline, not only an unrelated inspiration image.

A missing browser/screenshot facility is a blocker to visual proof; successful HTML extraction or build is not a substitute. Static video samples demonstrate appearance only, not working interactions.

## Interaction review

Exercise the primary user action, loading/empty/error/success states and relevant keyboard paths. For a form, check validation, double submission and success feedback. If persistence is relevant, write → authoritative read/reload → observe the same record. Inspect denied/unauthorized behavior when the change touches it. A successful write followed by a UI error is not automatically data loss; inspect the authoritative state.

Preserve approved functionality during cosmetic changes. Re-run affected checks after the final correction. Avoid arbitrary coverage targets or hundreds of unrelated tests, but do not transfer all testing to the user.

## Feedback and handoff

One issue per note: target element/state/viewport, observed behavior, expected behavior, evidence and priority. Use Agentation when already available; a manual note is sufficient. Do not reopen approved macrostructure unless the user requests it or a demonstrated constraint makes it impossible.

Report exact checks/results, visual evidence or blocker, source changes, remaining decisions and release classification. A concept, local runtime-proven candidate and deployed release are different states. Stop temporary services unless the user requested keeping them. No publish/push/deploy permission is created by completing UI proof.
