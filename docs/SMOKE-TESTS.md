# Speedtest / Looking Glass / Route Server smoke checks

## Scope

Python 3.10+ (stdlib only). This is a **read-only diagnostics tool**, not a production application patch or load/throughput test. Run it **locally on the relevant, authorized VM**, not across the public Internet. No service restarts, package installs, route changes or BGP mutations.

| Profile | Checks |
|---|---|
| `speedtest` | Ookla and native app systemd state, TCP 5060/8080, native app health JSON and OpenAPI start-test route on 127.0.0.1:8095 |
| `lg` | `teknotel-lg` and `cloudflared` systemd state; local FastAPI OpenAPI JSON on 127.0.0.1:8080 |
| `rs` | `gobgpd` systemd state and GoBGP neighbor state summary (minimum two Established peers by default) |

```sh
python3 tools/service_smoke.py --profile speedtest --json
python3 tools/service_smoke.py --profile lg --json
python3 tools/service_smoke.py --profile rs --expect-peers 2 --json
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Exit status: 1 if any check FAIL; 0 otherwise. WARN is non-fatal and indicates a need to review unrecognized GoBGP output. No peer IPs, service raw logs, client measurements or keys are printed. The tool intentionally does not test public reachability, gRPC authorization, network throughput, BGP export policy, FlowSpec functionality, Cloudflare Access or production configuration compliance.

## Known limitations

- Local loopback health does not establish externally accessible or healthy public traffic.
- The GoBGP state parser recognizes the human-readable neighbor table only if each peer row starts with an IP address. Unknown formats return WARN, not a false healthy result.
- Speedtest `/api/health` HTTP 200 and JSON syntax do not independently prove application-level fitness; a later source review can tighten semantics.
- Endpoint selection and timeout values match the October 2026 operator inventory; validate those assumptions before production adoption.
- This script does not write or modify any application source or configuration.

## Verification

Static syntax compile and 13 isolated unit tests passed locally on 2026-11-03. This does **not** mean tests were run on Speedtest, LG or RS production hosts. Any production verdict must be based on separately captured on-host checks.
