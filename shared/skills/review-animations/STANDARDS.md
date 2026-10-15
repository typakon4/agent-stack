# Animation Standards Reference

Local condensed reference adapted from Emil Kowalski's animation standards. Use the project's existing implementation and verify the actual rendered behavior.

## Purpose and frequency

Motion should communicate spatial relationships, state, explanation, or feedback. Keyboard-initiated actions and actions repeated hundreds of times daily usually remain immediate. Reduce motion for frequent interactions; occasional modals and toasts can use standard transitions; rare onboarding and celebrations can carry expression.

## Timing and curves

- Entering or exiting: ease-out. Moving or morphing: ease-in-out. Hover and color: ease. Constant motion: linear.
- Strong UI ease-out: cubic-bezier(0.23, 1, 0.32, 1).
- On-screen ease-in-out: cubic-bezier(0.77, 0, 0.175, 1).
- Drawer curve: cubic-bezier(0.32, 0.72, 0, 1).
- Button press feedback: 100–160ms; small tooltips and popovers: 125–200ms; dropdowns: 150–250ms.
- Keep ordinary UI transitions below 300ms unless a specific interaction justifies more time. Marketing storytelling can be slower.
- Slow the deciding part of an interaction and accelerate its response. Make repeated tooltips immediate after the first reveal.
- Group entrances can stagger by 30–80ms while all controls remain interactive.

## Physicality and interruption

Start a appearing element near scale 0.9–0.97 with opacity rather than scale zero. Popovers grow from their trigger; centered modals can retain a centered origin. Press feedback commonly uses scale 0.95–0.98.

Prefer interruptible transitions for rapid changes. Springs preserve velocity across interruption and suit reversible gestures; keep bounce restrained and reserve stronger bounce for playful interactions.

For swipes, consider velocity as well as distance. Apply resistance at boundaries, maintain pointer capture during the gesture, and protect the active gesture from extra pointers. Avoid abrupt invisible barriers.

## Performance

Transform and opacity usually avoid layout and paint. Measure other properties on the actual target when needed. Changing a parent CSS variable to drive descendants can recalculate their styles; update the relevant element directly when practical.

Check whether the project's animation library executes transform shorthands on the main thread. Prefer full transform values when its supported acceleration path requires them. CSS and the Web Animations API can deliver predetermined motion with little JavaScript overhead.

Translate percentages follow the element's size. Scaling also scales children. Clip-path can reveal, compare, or transition matching surfaces; heavy blur is costly, especially on Safari.

## Accessibility and evidence

Respect reduced-motion preferences and preserve transitions that aid comprehension with gentler opacity or color changes where appropriate. Gate hover effects to devices that support accurate hover.

Inspect slow motion, frame-by-frame timing, origin, and coordinated properties when feel is uncertain. Test gesture behavior on actual devices when available and report what remains emulated or untested.

Match motion to product character and existing tokens. Professional task UI often benefits from crisp restrained movement, while playful or expressive surfaces may justify a different rhythm.

