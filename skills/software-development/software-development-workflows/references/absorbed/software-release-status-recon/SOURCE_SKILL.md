---
name: software-release-status-recon
description: Verify whether a software feature/app is real, runnable, released, or just announced by triangulating docs, source tree, commits, build scripts, and release artifacts.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [release-status, github, desktop-apps, installer, verification, software-recon]
---

# Software Release Status Recon

Use this skill when the user asks questions like:

- “Is this app actually launched or just marketing?”
- “What is going on with the Windows/native/desktop version?”
- “Can people run it now?”
- “Is there an installer/release, or only source code?”
- “Summarize the state of a project’s rollout from GitHub/docs.”

The goal is to give a grounded status, not hype. Distinguish **implemented in source**, **documented**, **buildable/runnable**, and **published as a user-facing release artifact**.

## Workflow

1. **Load any project-specific skill first**
   - If the project is Hermes Agent, load `hermes-agent` first.
   - If a project-specific skill is protected/bundled, do not patch it; use this umbrella for reusable recon patterns.

2. **Check past context if relevant**
   - Use session search when the user asks “what happened with X” and prior conversations may contain context.
   - Do not let old context override current upstream state; treat it as hints only.

3. **Check official docs and source**
   - Official docs: install guide, platform guide, feature page.
   - Source tree: does the feature/app directory exist?
   - README/package/build scripts: can it be run or built?
   - Recent commit history: is it actively developed or stale?

4. **Check release artifacts separately**
   - GitHub source code presence is not the same as a published installer.
   - Query releases/latest or inspect release assets.
   - Explicitly list whether expected artifacts exist: `.exe`, `.msi`, `.dmg`, `.AppImage`, `.deb`, `.rpm`, wheels/tarballs, etc.

5. **Separate status levels in the answer**
   - **Native support / feature code:** present or absent.
   - **Runnable from source/CLI:** yes/no/unknown.
   - **Prebuilt installer:** yes/no/partial.
   - **User-ready rollout:** shipped, beta, manual build, docs-only, or unclear.

6. **Mention confidence and caveats**
   - Say when the docs claim something but release assets do not yet show it.
   - Say when `main` is ahead of the latest tagged release.
   - Avoid negative permanent claims like “doesn’t exist” when the more precise truth is “not present in latest release assets I checked.”

## Useful commands/patterns

For a local git checkout:

```bash
git fetch origin main --quiet
git rev-parse HEAD
git rev-parse origin/main
git ls-tree -r --name-only origin/main | grep '^apps/desktop\|windows-native\|install.ps1' | head -120
git show origin/main:apps/desktop/README.md | sed -n '1,220p'
git log --oneline -12 origin/main -- apps/desktop scripts/install.ps1 website/docs/user-guide/windows-native.md | cat
```

For release assets, prefer GitHub API or `gh release view` when authenticated:

```bash
python - <<'PY'
import json, urllib.request
url='https://api.github.com/repos/OWNER/REPO/releases/latest'
with urllib.request.urlopen(url, timeout=15) as r:
    d=json.load(r)
print('tag', d.get('tag_name'))
print('name', d.get('name'))
print('published', d.get('published_at'))
for a in d.get('assets', []):
    print('-', a.get('name'), a.get('browser_download_url'))
PY
```

## Answer shape for the user

Keep it compact and direct:

- “Short answer: yes/no/partially.”
- “What is real now:” bullets.
- “What is not yet fully shipped:” bullets.
- “Practical status:” one-liner.

For Telegram-style users, avoid tables; use bullets and labels.

## Pitfalls

- Do not equate docs copy with installed reality.
- Do not equate source tree with prebuilt release availability.
- Do not equate a latest release’s missing installer with “the feature is fake”; `main` may be ahead.
- Do not over-explain build internals unless the user asks; most users want rollout status.

## References

- `references/hermes-windows-desktop-recon-2026-06-02.md` — example of triangulating Hermes Windows/Desktop state from docs, source, commits, and GitHub release assets.
