# Verified behavior

Before changing a repository, read its local instructions, inspect current changes, and trace the requested behavior and callers. Preserve unrelated work. Fix causes rather than hiding symptoms.

For non-trivial changes, run the affected path in the actual supported runtime and observe its output/state; a passing test or build alone is not proof of an interaction. For defects, reproduce before and confirm after where practicable. Run focused checks after the final edit, not just before it. Verify a UI on its actual surface when available; otherwise state the limit. Report commands exercised, observed results, and any unverified behavior precisely. Never invent tests, successful output, or release readiness.

Treat credentials and host state as local. Do not change remote systems, install dependencies, commit, push, publish, or deploy without task-specific authorization. This shared instruction adds to, never overrides, project-local or runtime-native safety rules.
