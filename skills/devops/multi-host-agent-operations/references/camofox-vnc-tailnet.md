# Persistent Camofox live browser over Tailscale

Use this when an always-on VPS needs a human-visible browser for a legitimate interactive login, while its control API and raw VNC must stay private.

## Security boundary

- Keep Camofox control API (`9377`) on `127.0.0.1`.
- Keep raw `x11vnc` on `127.0.0.1`/`::1` (`-localhost`), even if noVNC is reachable over the tailnet.
- Bind noVNC/websockify to the VPS Tailscale address (not `0.0.0.0`), e.g. `VNC_BIND=100.x.y.z`.
- Prefer `http://<tailscale-ip>:6080/vnc.html?autoconnect=true&resize=scale&path=websockify` from a device already in the same tailnet. Do not publish an interactive browser route through public Caddy just for convenience.

## Camofox VNC plugin service environment

The VNC plugin requires both inclusion/enabling in `camofox.config.json` and `ENABLE_VNC=1` in the service environment. A known-good systemd override has:

```ini
[Service]
Environment=ENABLE_VNC=1
Environment=VNC_BIND=100.x.y.z
Environment=VNC_PORT=5901
Environment=NOVNC_PORT=6080
Environment=VNC_RESOLUTION=1920x1080
Environment=TAB_INACTIVITY_MS=43200000
Environment=SESSION_TIMEOUT_MS=43200000
Environment=BROWSER_IDLE_TIMEOUT_MS=43200000
Restart=always
```

The 12-hour timeouts matter: noVNC mouse/keyboard input does not increment Camofox tool-call activity. Defaults can reap a live human-login tab after five minutes and make the browser look like it is repeatedly reloading.

## Verify

1. Restart the service and verify `6080` binds only to the configured Tailscale IP; `5901` must remain loopback-only.
2. From a tailnet peer, run `tailscale ping <vps-tailnet-ip>` and open the noVNC URL.
3. Confirm Camofox has an active tab/session; keep the tab open during interactive work.
4. Let the user complete passwords, 2FA, CAPTCHA, and consent prompts. Do not type secrets or click those controls.

## Implementation pitfall

Some Camofox VNC watcher versions log to `/var/log/novnc.log` and `/var/log/x11vnc.log`. A non-root systemd service cannot write there, causing watcher exit/reconnect loops. Redirect those logs to `${TMPDIR:-/tmp}` or a service-writable log directory before relying on live view.
