---
name: typakon4-motion-anti-slop
description: "Quality gate for proof-first typakon4 social motion visuals."
version: 1.0.0
platforms: [linux]
metadata:
  hermes:
    tags: [motion, visual-design, social, quality-gate, hyperframes]
---

# Typakon4 Motion Anti-Slop Gate

## When to use

Use before designing, editing, or rendering a typakon4 social visual, motion graphic, article cover, explainable diagram, or short trailer.

This is a **quality gate**, not an automatic visual generator. It applies before selecting HyperFrames, Remotion, SVG/PIL, or another renderer.

## Non-negotiable creative contract

1. Name the visual job before choosing a layout:
   - **click** — title-first editorial cover;
   - **save** — compact reference / mechanism card;
   - **proof** — real redacted chart, screenshot, trace, or source artifact;
   - **understanding** — one causal flow;
   - **identity** — restrained recurring typographic/material language.
2. One frame gets one dominant reading object. The title, map, chart, or comparison must win at thumbnail scale.
3. A visual claim must have an evidence status: **real artifact**, **sourced fact**, **design interpretation**, or **conceptual explainer**. Never disguise one as another.
4. Default: motion should reveal a causal path, state transition, or comparison that the static frame cannot express honestly. **Exception — declared identity/stop-scroll motion:** a visual may be deliberately sensory “brain-chewing” material whose job is to make the reader pause and read. In that lane, motion need not explain a system, but it must not impersonate runtime proof, product UI, or evidence.
5. Start static-first. Freeze and inspect the opening frame before spending time on animation.

## Reject these defaults

Do not ship:

- generic AI heads, brains, robots, glowing networks, or invented terminals;
- faux SaaS dashboards, equal-weight cards, fake metrics, made-up traces, or product UI without a real product artifact;
- decorative gradients, glassmorphism, glow pulses, rainbow status colors, cyberpunk clutter, or busy background grids;
- centered-webpage layouts with tiny copy and enormous empty middle space;
- motion that is only a sequence of card pops, bouncing springs, generic micro-interactions, or fast position jumps;
- a `Codex ↔ Hermes` architecture picture when the post lacks a real verified handoff/receipt;
- a dense explainer grid masquerading as an article cover.

## Typakon4 material language

- Default toward light/off-white editorial or dark flat editorial only when the topic/job demands it.
- Choose the active signal color from the topic/material palette; **cyan is an option, not a default**. It must earn contrast and a semantic role. Red marks rejection, return, or failure only.
- Typography is the hero; routes, dots, packets, and lines are supporting evidence.
- Prefer type-first anchors over rounded product cards or logo tiles.
- Use labels only when they add a distinct information job. Remove duplicate labels.
- A conceptual visual must state/behave as conceptual; runtime proof requires a real and pixel-audited artifact.

## Motion language

Use calm, continuous travel:

```text
title settles once
→ one signal physically travels a meaningful route
→ one local state becomes active
→ it settles quietly
```

- Use opacity and 6–10px restrained translations for reveals.
- Use one focal event at a time.
- Moving dots must never cover headline or critical labels.
- No bounce, spring pop, glow pulse, rainbow transition, abrupt teleport, or infinite busy loop.
- End with a legible hold; never fade the conclusion before the video ends.

## Renderer choice

- **HyperFrames:** short 6–15 second HTML/CSS/SVG/GSAP editorial motion and deterministic visual QA.
- **Remotion:** existing canonical React compositions, reusable data-driven components, or established local projects.
- **SVG/PIL/FFmpeg:** bounded fallback when a project setup would cost more than the artifact.

Do not install, update, or import third-party renderer skills automatically. The vendor HyperFrames core creative/animation packs require a separate security review before use. Prefer a project-local pinned renderer version. Do not let `init` silently alter global skills.

## Pre-render gate

Before rendering, answer all of these in the composition brief:

```text
Visual job:
Dominant reading object:
Reader action: click / save / understand / trust
Evidence status:
What motion proves:
What is intentionally absent:
```

If the answers are vague, stop and simplify the board.

## Verification gate

1. Render/inspect opening, signature-move, and closing frames at delivery size.
2. Audit pixels for secrets, private paths, fake runtime claims, illegible microcopy, overlap, and accidental UI-looking clutter.
3. Ask whether the frame would still work as a static post. If not, fix the composition before adding more motion.
4. For HyperFrames projects, use the project's pinned local CLI and run its available visual checks (at minimum lint/check/snapshots) before publishing.
5. Report the actual artifact path, resolution, duration, fps, checked frames, and remaining limitations.

## Stop conditions

- If there is no honest visual artifact for a proof claim, publish text/source media or skip the visual.
- If the idea needs a taxonomy, use a static mechanism grid; do not force it into a kinetic trailer.
- If the user rejects the visual family, return to a frozen static keyframe instead of endlessly tuning animation.
