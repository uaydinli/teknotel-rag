# LG Atlas adapter review — 2026-10-23

Source: operator-provided `atlas_api.py` excerpt and Cloudflare service/file metadata. Static review only.

## OBSERVED
- Atlas API v2 via HTTPX, timeout 15s, redirects disabled.
- Probe allowlist contains three named locations: Eminonu/Istanbul, Kizilay/Ankara, Atasehir/Istanbul.
- Measurement supports ping, traceroute and DNS, one-off IPv4.
- Shared quotas: 30 attempts per hour and 200 per day, persisted in SQLite. Repeated request signature reused for 300s.
- Atlas key read from a local configurable file; no secret value shown.
- Ping/traceroute target normalization rejects non-global IPv4 after hostname resolution; DNS uses hostname validation.
- POST measurement gate checks custom x-lg-atlas header and sec-fetch-site not equal cross-site.
- SQLite BEGIN IMMEDIATE transaction remains open across synchronous outbound Atlas creation request; potential write contention under concurrency.
- cloudflared.service active; two config YAMLs and credential artifacts present under a user's .cloudflared directory (filenames not published here).

## ASSESSMENT
- Header and Fetch Metadata checks are not equivalent to authenticated user identity; Cloudflare Access/WAF rules remain unverified.
- No secrets or raw tunnel configuration should be placed in this public repository.
- No active vulnerability exploitation, production modification or external measurement creation performed.

## NEXT
- Inspect sanitized tunnel ingress mapping (hostname and origin port only), without exposing credentials.
- Check Access/WAF configuration separately where authoritative data is available.
- MTR future scope tracked in docs/LG-DEVELOPMENT-BACKLOG.md.
