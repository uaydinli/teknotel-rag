# Project scope — Speedtest / LG / RS

Date: 2026-10-23
Status: Initial discovery and repository organization

This is a shared, persistent, evidence-first engineering repository for the three project areas below. It is not yet a vector database. Git history stores changes; Markdown evidence records are independently searchable with `tools/rag_search.py`.

| Area | Purpose | Status |
|---|---|---|
| `speedtest` | Ookla Speedtest server investigations, native browser Speedtest, testing and performance evidence | Discovery pending |
| `lg` | Looking Glass source code, network diagnostics and integration evidence | Discovery pending |
| `rs` | Route Server: BGP routing policy, peer/session diagnostics, configuration and development evidence | Project identity confirmed; deployment and software stack not yet verified |

## Evidence format
Each dated investigation should record:
- `OBSERVED`: command, configuration, file or externally received document actually inspected.
- `INFERRED`: reasoned interpretation, explicitly supported by observations.
- `HYPOTHESIS`: unverified explanation.
- `VERIFIED`: reproducible test and its output, or authoritative configuration.

Capture source identifier, observation date, environment, redacted command/output, change and validation. Append corrections; do not erase earlier records.

## Repository boundaries
- Public GitHub content is not a secrets store, telemetry database or backup location.
- Never commit private keys, passwords, tokens, customer data, unredacted PCAPs or private server configuration.
- Record the existence, hash and access-controlled storage location of sensitive artifacts instead of their raw bytes.
- Place verified source code under `projects/<area>/` when it becomes available; until then avoid inventing deployable code.
- Preserve existing Graylog and other infrastructure evidence and their established audit rules.

## Next discovery inputs
- Read-only inventory of Speedtest services, runtime and browser code.
- Looking Glass application source, network test endpoints and observed deployments.
- Route Server implementation inventory: routing daemon, BGP peers, policy model, processes and dependencies.
