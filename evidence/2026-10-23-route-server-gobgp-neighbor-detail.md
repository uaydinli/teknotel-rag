# Route Server GoBGP — Detailed Neighbor Discovery
Date: 2026-10-23
Source: operator-provided output of `gobgp neighbor <peer>`, CLI help and `ps -C gobgpd`
Evidence type: OBSERVED, with explicit limitations

## Runtime
- GoBGP daemon v4.9.0 (previous evidence)
- Process PID 1444, elapsed 2d 22:55:53; ps CPU 8.6%, MEM 17.6%, RSS 2889048 KiB
- GoBGP exposes CLI gRPC host default 127.0.0.1:50051 per help (this is CLI default, not independent socket verification).

## Peer A (private neighbor IP redacted; AS25145)
- SESSION_STATE_ESTABLISHED; uptime 2d 22:49:49, OutQ 0, Flops 0.
- Router ID redacted (public-looking address but not needed in public evidence).
- Route statistics: Advertised 0; Received 1121789; Accepted 1121789.
- Message statistics: Opens sent 54/received 54; Notifications sent 0/received 53; Updates sent 1146637/received 1762475; Keepalives sent 8553/received 1; Discarded received 1.
- Capability negotiated both directions: IPv4 unicast, IPv4 FlowSpec, route refresh, 4-octet AS.
- Graceful restart and long-lived graceful restart received. Extended message advertised locally only.

## Peer B (private neighbor IP redacted; AS25145)
- SESSION_STATE_ESTABLISHED; uptime 2d 22:50:42, OutQ 0, Flops 0.
- Route statistics: Advertised 0; Received 1121831; Accepted 1121831.
- Message statistics: Opens sent 1/received 1; Notifications sent 0/received 0; Updates sent 1619118/received 2723916; Keepalives sent 8502/received 1; Discarded 0.
- Capability negotiated both directions: IPv4 unicast, IPv4 FlowSpec, route refresh, 4-octet AS.
- Graceful restart and long-lived graceful restart received. Extended message advertised locally only.

## OBSERVED / UNKNOWN
- Both peer summaries show Advertised=0; do not infer an export-policy misconfiguration from this alone.
- Peer A has 53 received notifications, without timestamps/reason codes in the supplied output. Not enough evidence to attribute their cause or declare current session unstable.
- FlowSpec is negotiated, but no FlowSpec route-table sample or forwarding action verification was supplied.
- CLI help `gobgp policy neighbor` lists add/del subcommands, not a read/list subcommand; avoid assuming `gobgp policy neighbor` lists policy attachments.
- `gobgp global rib` has `-a` address-family and `summary` command; no FlowSpec summary has yet been observed.

## Next read-only work
- Capture bounded journal evidence for historical notifications without private contents in the public repository.
- Check FlowSpec RIB summary with CLI-supported AFI syntax and no full RIB dump.
- Inspect config for explicit policy assignments, after redaction.
