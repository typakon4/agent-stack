# Hermes mapping

Install shared skills and `personal-operator-baseline` only to a chosen **existing Hermes profile root** through the manifest and dry-run. Copying a skill does not enable a model, desktop app, gateway, or profile. The SOUL fragment is **manual**: compare with the target profile's actual SOUL and merge compatible text by hand. Do not overwrite upstream Hermes files, service configuration, local browser/auth state, or Telegram ownership. Installing PC Hermes is not part of this repository.

Jev is a separate pinned checkout. Hermes uses a thin, manually configured plugin integration plus Jev MCP tools where supported by the local Hermes version; this repo provides neither plugin code nor credentials. Leave Jev replay and traces on the profile host. Do not install a second connector beside a working local one. See `integrations/jev/README.md` from the repository root.
