# Looking Glass application inventory — 2026-10-23

Evidence source: operator-provided CLI output. Public-safe high-level inventory, no secrets.

## OBSERVED
- Service `teknotel-lg`: active, user teknotel, WorkingDirectory `/opt/teknotel/lg/app`, systemd unit at `/etc/systemd/system/teknotel-lg.service`.
- Backend Uvicorn PID 155695: cwd `/opt/teknotel/lg/app`, `main:app`, localhost port 8080.
- Python `http.server` PID 155594: cwd `/opt/teknotel/geofeed`, localhost port 8091.
- `cloudflared` active. Tunnel ingress mapping not yet inspected.
- Backend files include `app/main.py`, `app/gobgp_client.py`, `app/atlas_api.py`; multiple backup variants present.
- Web files include `web/index.html`, `web/app.js`, `web/atlas.js`, `web/style.css`, `web/speedtest-native.js`.
- Separate Speedtest directory contains `engine.js`, `cors.py`, `install-lg.py`, `test-dom.cjs`, README.
- Bundled `gobgp-src` contains upstream Go source tree including .git metadata; not assumed to be application-owned code.
- Python versions: fastapi 0.141.1, uvicorn 0.53.0, starlette 1.6.0, pydantic 2.13.5, httpx 0.28.1.
- Local API `/openapi.json` responded HTTP 200.
- `git rev-parse --is-inside-work-tree` gave no positive output in either application path; actual working-tree status still unverified.

## NOT YET VERIFIED
- Route definitions, authentication, commands executed by API, exact frontend/backend integration, tunnel ingress mapping, source provenance, test coverage.
- No source code was copied to GitHub; avoid posting configurations, credentials or user data.

## NEXT
- Export a sanitized API route inventory from OpenAPI JSON, including method/path only.
- Inspect service metadata and file hashes, and manually review source for secrets before uploading.
