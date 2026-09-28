# Jev — external dependency, not vendored

External Jev repository: https://github.com/typakon4/jev-layer ; pinned commit: `08473a5496864e8c97ee6f8f58980131ae16aed2`. `manifest.yaml` (`jev.repository`, `jev.commit`) is authoritative; review upstream changes separately before changing the pin. This repo contains **no** Jev source, plugin bundle, MCP config, runtime credentials, replay, or trace data, and it does not fetch or update Jev.

Hermes integration is a thin runtime-local plugin plus MCP, installed/configured only by its owner against the selected Hermes version. OMP uses its **existing** Jev stdio MCP; Codex connects to Jev via its own MCP configuration. This repository changes none of those configurations or registers a duplicate endpoint. Jev recommendations are advisory; the host decides what, if anything, to execute. Keep execution receipts/replay and credentials on the host, never in this repository.
