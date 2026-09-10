---
name: motion-explainer-production
description: Produce and refine proof-first social motion explainers with Remotion or equivalent code-based video tools, from static keyframe through verified MP4.
version: 1.0.0
---

# Motion explainer production

Use this skill for code-based social explainers, especially square Remotion videos that must be readable as a static social card and still gain meaning from motion.

## Design premise

A motion explainer has two separate tests:

1. The opening frame must work at feed/thumbnail scale without motion.
2. Animation must reveal a causal relationship, state transition, or execution path that a static image cannot convey as clearly.

Do not use animation to compensate for a weak board, an unclear hierarchy, or a generic dashboard layout.

## Intake and discovery

1. Inspect the existing composition, source files, available fonts, render scripts, and prior previews before editing.
2. If the user supplied multiple videos, extract or inspect opening, middle, and closing frames before proposing a redesign.
3. Identify whether the user wants a **polish** or a **new visual family**. Do not infer redesign authorization from dissatisfaction with a small defect.
4. Name the visual job before designing:
   - title-first Article cover;
   - saveable reference card;
   - causal process explainer;
   - real execution-trace visual.

## Canonical-composition rule

When a user says a prior render is clearer, more elegant, or more compelling, treat that render as the canonical composition.

A canonical polish pass may adjust:

- branding;
- type hierarchy and font consistency;
- geometry and alignment;
- card spacing;
- z-index/collision issues;
- restrained color use;
- easing and timing.

It must not change, without explicit approval:

- composition topology;
- the number of primary objects/cards;
- title scale or reading order;
- the visual family;
- the density and negative-space balance that made the version successful.

Write the brief as `repair, not redesign` and explicitly forbid using rejected variants as visual references.

## Static-first workflow

1. Freeze a still keyframe at the actual delivery size (normally 1080×1080 for a square social post).
2. Audit it at thumbnail scale. The title must be the dominant readable object. Remove any microcopy, ornamental metadata, or duplicate labels that cannot survive the scale.
3. Check the information architecture. Repeated equal rows, pills, labels, and connecting lines often read as a policy table or fake product UI, not a story.
4. Only after the still works, animate a single causal path, state change, or reveal sequence.
5. Render a real MP4 and inspect the opening, midpoint, and final frame. Treat the exact last frame as a separate closure test: the takeaway must remain readable after routes/signals settle; do not fade every explanatory element into an empty end card.
6. If no approved Remotion project exists, use an equivalent code-based renderer only when the user asked for an actual media artifact. Keep the render source alongside the MP4 and record dimensions, fps, duration, and frame-QA result. Never substitute a prompt/brief for a render.
7. Never report a render as successful without the artifact.

## Composition and typography

- Let each visual have one dominant reading object: usually a title, one loop, one graph, or one central comparison.
- Use display typography for the headline and major conceptual labels. Restrict mono/small system typography to metadata, counters, and quiet annotations.
- Avoid making all labels equal in weight; equal labels produce UI noise.
- Do not duplicate the same action in a condition card, a central column, and a destination card. Every element must have a distinct information job.
- Keep a social cover title-first. Put the complete map or system explanation in a separate in-article or saveable visual.

## Path, dot, and layering discipline

- A moving dot should show the currently active causal route, not wander decoratively.
- Use one active focal event at a time.
- Route dots around critical labels whenever possible.
- Explicitly test z-index and collision: moving dots, lines, cards, and nodes must not obscure the title or a key label. Layering text above a route is acceptable only when the path still reads cleanly.
- A path must communicate a transition. Do not add diagonal lines, rings, or loops merely to create activity.

## Motion language

Default motion language:

- calm entry for title;
- continuous path travel for active signals;
- soft route drawing;
- subtle opacity plus 6–10px vertical reveal for cards;
- restrained `cubic-bezier(0.22, 1, 0.36, 1)` easing;
- state settles after an event rather than pulsing forever.

Avoid:

- bounce or spring-pop behavior;
- generic dashboard micro-animations;
- abrupt position jumps;
- glow pulses;
- gradients used as visual filler;
- rainbow status palettes;
- animating every element at once.

## Proof-first media gate

Do not manufacture technical proof with generated terminals, fake traces, invented tool UI, fictitious metrics, or made-up model outputs.

For a runtime/execution visual, use only supplied and safely redacted events. Build it from a data array so the composition can later render a genuine trace. Until such an artifact exists, label the asset as a conceptual explainer, not a demonstration.

## Visual review and iteration

When the user reacts negatively, do not defend the previous design with theory. State the concrete failure and pick one of these paths:

- **polish:** the canonical composition works; fix only specific defects;
- **revert:** an earlier composition was demonstrably stronger; freeze it and discard later variants;
- **change concept:** the subject is a list/table but is being forced into a motion narrative; choose a different visual job or make a static card instead.

Do not enter an endless `render → cosmetic tweak → render` cycle. After a concept-level rejection, return to a static keyframe review before another full motion render.

### Cost-bounded exploratory renders

When the user asks for a quick model/renderer probe, or explicitly prioritizes token/cost economy:

1. Do **one bounded implementation + one real render**. Confirm only that the build/render command completed and an artifact exists; do not add vision QA, repeated frame extraction, or speculative rerenders unless the user asks for review.
2. Send the first artifact immediately, even if it is visibly weak. A probe's value is that the user can judge it directly.
3. Preserve the source and rendered media until the user explicitly says to delete them. A negative reaction is feedback, **not** deletion authorization.
4. Keep delivery short: artifact, format/duration, and one honest sentence about what was delegated. Do not spend the token budget defending an unsuccessful visual.
5. For code-agent trials, delegate implementation mechanics (Remotion components, path math, timing, and rendering) rather than asking the model for unconstrained art direction. Keep composition/taste in a human-approved static brief.

## Delivery checklist

Before handing off:

- [ ] Original/canonical composition was preserved.
- [ ] Scope was confirmed as polish or redesign.
- [ ] Opening frame is legible at thumbnail scale.
- [ ] Main title is unblocked by moving elements.
- [ ] No duplicate labels or fake-dashboard clutter remain.
- [ ] Motion has one visible causal purpose.
- [ ] Rendered MP4 exists at requested dimensions, fps, and duration.
- [ ] Opening, midpoint, and final frames were inspected.
- [ ] Render command and composition name are reported.
