# Interface resilience

Local static adaptation of Impeccable's hardening playbook. Keep changes within the requested interface work and use the project's existing implementation and test tools.

## Content and layout

- Exercise long and short names, empty content, emoji, RTL and CJK text, large numbers, many items, and narrow containers.
- Allow flex and grid children to shrink with a minimum inline size of zero where necessary. Choose wrapping, single-line ellipsis, or line clamping based on whether the full content must remain available.
- Let text containers grow. Keep controls usable at 200 percent zoom and under platform text scaling.
- Budget for translation expansion and use logical spacing properties for RTL layouts. Format dates, numbers, currencies, and plural forms through the existing internationalization system.

## Status and recovery

- Cover initial and paginated loading, empty lists, no search results, validation failures, unavailable network, slow requests, expired sessions, denied permissions, and rate limits where these states apply.
- Preserve entered data on recoverable errors. Place field-specific errors near their inputs and give a clear recovery action.
- Prevent duplicate submission while an operation is pending. Ensure stale responses and optimistic updates cannot silently overwrite newer state.
- Keep unaffected parts of the interface usable when one component fails.

## Interaction and access

- Cover keyboard focus, tab order, meaningful labels, dynamic announcements, high contrast, and alternatives to color-only status.
- On custom drag surfaces, test a second pointer, cancelled gestures, lost pointer capture, release outside the control, and window focus loss. End or retain the correct interaction, release capture, and confirm the next interaction works.
- Respect existing permissions and maintain a clear distinction between available and unavailable actions.

## Delivery and evidence

- Check representative states through the actual supported surface. Use emulated viewports and input where useful, and state which physical devices or engines were not tested.
- Load large datasets progressively or through existing virtualization. Clean up listeners, timers, subscriptions, and obsolete pending requests.
- Use the project's established validation and test runner when a confirmed behavioral change requires regression coverage.
- Describe the observed recovery, overflow, focus, localization, and interaction results. A checklist without observed evidence does not establish completion.

