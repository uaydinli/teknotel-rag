# Route Server GoBGP runtime discovery — 2026-10-23

Source: operator-shared read-only output captured in /root/rs-discovery-20261023T140045Z. Local collection timestamp: 2026-10-23 14:00 UTC.
Status: OBSERVED except where marked otherwise. Private peer and router IPs omitted in this public repository.

## OBSERVED — runtime
- gobgpd version: 4.9.0
- `gobgp version` returned exit 1: unknown command "version" for "gobgp". This is CLI syntax, not daemon failure.
- systemd gobgpd: LoadState=loaded, ActiveState=active, SubState=running; unit path /etc/systemd/system/gobgpd.service.
- Global: local AS 65004; BGP TCP port 179; listening on 0.0.0.0 and ::; private Router-ID redacted.
- Peer A: private IP redacted, remote AS 25145, Established, uptime 2d 22:43:22, Received=1121776, Accepted=1121776.
- Peer B: private IP redacted, remote AS 25145, Established, uptime 2d 22:44:09, Received=1121818, Accepted=1121818.
- IPv4 unicast global RIB summary: Destination=1121828, Path=2243594.
- IPv6 unicast global RIB summary: Destination=0, Path=0.
- `gobgp policy` and `gobgp policy statement` generated empty outputs; `gobgp policy prefix` reported "Nothing defined yet".
- Both neighbors are configured with IPv4 unicast and IPv4 flowspec AFI/SAFI (earlier operator-shared TOML), eBGP multihop TTL 5, hold 90s and keepalive 30s.

## Interpretation / limitations
- OBSERVED: Received equals Accepted in the neighbor summary for both peers.
- INFERRED: There is no evidence yet in the collected outputs of named import/export filtering rules.
- NOT VERIFIED: active neighbor policy assignments, Adj-RIB-Out, FlowSpec RIB content, export actions, negotiated capabilities, traffic forwarding/filtering behavior.
- Do not equate configured FlowSpec capability with active FlowSpec routes; do not equate empty policy-list output with proof of all policy enforcement being absent.

## Next read-only verification
Review detailed neighbor and policy assignment outputs, FlowSpec RIB summary, and bounded Adj-RIB-Out samples/summary. Avoid full route table dumps, configuration changes or session resets.
