# Route Server / GoBGP — initial discovery

Date (UTC): 2026-10-23
Source: operator-provided interactive terminal transcript
Status: partial discovery; session and RIB outputs not yet provided

## OBSERVED
- Host prompt: `rs`; OS login banner: Ubuntu 24.04.4 LTS; kernel `6.8.0-147-generic`.
- `gobgpd` process is running as root with `/usr/local/bin/gobgpd -f /etc/gobgp/gobgpd.toml` (process started Oct 20 according to `ps`).
- Configuration has local AS `65004`, TCP BGP port `179`, and a private IPv4 router ID (exact internal address omitted from public evidence).
- Two configured neighbors (peer-A and peer-B; private addresses redacted), both remote AS `25145`.
- Both neighbors: eBGP multihop enabled, TTL 5; hold 90s, keepalive 30s, connect retry 30s; IPv4 unicast and IPv4 FlowSpec AFI/SAFI.
- Read-only discovery command summary: `gobgp version` exited 1; `gobgpd --version`, `gobgp global`, `gobgp neighbor`, IPv4/IPv6 RIB summary and policy commands exited 0.
- Discovery archive created locally at `/root/rs-discovery-20261023T140045Z.tar.gz`, not uploaded to repository.

## NOT YET VERIFIED
- GoBGP daemon version string, neighbor session state, negotiated AFI/SAFI, route counts, import/export policy and runtime RIB content: output files exist but their contents were not provided.
- `gobgp version` exit 1 is **not** evidence of daemon failure; capture its stderr/usage text.
- No conclusion about whether FlowSpec routes are actually advertised or accepted.

## NEXT
Review sanitized `gobgpd_version.txt`, `gobgp_version.txt`, `gobgp_global.txt`, `bgp_neighbors.txt`, `rib_ipv4.txt`, `rib_ipv6.txt`, `gobgpd_service.txt`, and policy text files. Do not publish exact internal addresses or full configuration without explicit review.

## Security
Repository is public; raw config, private addresses, credentials and complete routing data remain outside GitHub pending redaction.
