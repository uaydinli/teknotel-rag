# Looking Glass ingress checkpoint — 2026-10-23

Source: operator-provided sanitized inspection of two cloudflared YAML files.

## OBSERVED
- `config.yml`: hostname `lg.teknotel.com` routes to local loopback port 8080. An additional service line was redacted.
- `geofeed-config.yml`: hostname `geofeed.teknotel.com` routes to local loopback port 8091. An additional service line was redacted.
- Earlier discovery mapped Uvicorn API to loopback 8080 and Python static HTTP server to loopback 8091.

## LIMITATIONS
- The command redacted non-loopback services; fallback ingress actions and Cloudflare Access/WAF policies remain unverified.
- No tunnel credential files, tokens, or sensitive config contents were collected.
- User requested transition to Speedtest server discovery. No LG changes deployed.
