# Hermes Windows/Desktop recon example — 2026-06-02

This reference captures a compact example pattern for answering “is Hermes Windows/Desktop real or just announced?”

## Evidence checked

- Loaded the project-specific `hermes-agent` skill first because the user asked about Hermes setup/usage.
- Searched past sessions for `Hermes Windows приложение движ Workspace desktop Windows`; no matching session context.
- Web search found:
  - official Windows Native Guide: `https://hermes-agent.nousresearch.com/docs/user-guide/windows-native`
  - GitHub desktop app path: `https://github.com/NousResearch/hermes-agent/tree/main/apps/desktop`
- Fetched `origin/main` in the local Hermes checkout because the local working tree was behind and did not yet contain `apps/desktop`.
- Inspected source tree on `origin/main` and found `apps/desktop/` with Electron/React app files, package scripts, README, assets, tests, and installer targets.
- Inspected `apps/desktop/README.md` from `origin/main`:
  - describes native desktop app for Hermes Agent;
  - says available for macOS, Windows, Linux;
  - supports chat, streaming tool output, side-by-side previews, file browser, voice, settings/onboarding;
  - `hermes desktop` builds/launches GUI against an existing install;
  - release installers are attached manually when shipped.
- Inspected `apps/desktop/package.json` from `origin/main`:
  - Electron app version around `0.15.1` in source checked;
  - has `dist:win`, `dist:win:msi`, `dist:win:nsis`, `dist:mac`, `dist:linux` scripts;
  - `build.win.target` includes NSIS and MSI.
- Checked latest GitHub release via API:
  - latest tag seen: `v2026.5.29.2`, version `0.15.2`;
  - assets contained only Python wheel and tarball, no `.exe`/`.msi`/desktop installer assets.
- Recent commit history showed active desktop work, including cancellable first-launch install, sidebar session search, session hygiene, media streaming, settings refactors.

## Answer conclusion pattern

Use this wording pattern:

- “Yes, the app is real: source and build scripts exist in `apps/desktop`, and docs describe native Windows support.”
- “Native Windows CLI/install is real: PowerShell installer, no WSL/admin required, installs under `%LOCALAPPDATA%\\hermes`, data under `%USERPROFILE%\\.hermes`.”
- “Desktop app is implemented/buildable from source and `hermes desktop` is documented.”
- “But latest public GitHub release assets checked did not include `.exe`/`.msi`; only wheel/tarball. So prebuilt Windows installer rollout may lag behind `main`.”
- “Practical status: Windows-native Hermes yes; Desktop source/app yes; one-click public Windows installer not verified in latest release assets.”

## Pitfall

Do not say “they launched the Windows app” without specifying which layer:

- Windows native CLI/support: yes.
- Desktop app in source/docs: yes.
- Prebuilt Windows installer in latest release assets: not verified / absent in checked latest release.
