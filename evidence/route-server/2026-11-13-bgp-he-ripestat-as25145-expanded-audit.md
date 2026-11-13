# AS25145 — bgp.he.net, RIPEstat and customer-prefix expansion audit

**Capture date:** 2026-11-13  
**Scope:** AS25145 public BGP state, selected IPv4 prefixes, AS51683 downstream relationship, IPv6 RPKI-invalid routes, RIPEstat collection method.  
**Evidence class:** Public route-collector observations, RIPE registry objects and third-party ASN/prefix dashboards.  
**Important:** This is not a live router configuration export. It does not prove production session state, router policy, traffic volume or forwarding behavior.

## 1. AS25145 snapshot from Hurricane Electric

Source: https://bgp.he.net/AS25145  
The page footer reports **Updated 12 Nov 2026 15:38 PST**.

| Metric | HE observation |
|---|---:|
| IPv4 prefixes originated | 71 |
| IPv6 prefixes originated | 81 |
| All prefixes originated | 152 |
| IPv4 prefixes announced | 79 |
| IPv6 prefixes announced | 81 |
| All prefixes announced | 160 |
| RPKI Valid, IPv4 | 67 |
| RPKI Valid, IPv6 | 68 |
| RPKI Invalid, IPv4 | 0 |
| RPKI Invalid, IPv6 | 13 |
| Observed BGP peers, all | 33 |
| Observed IPv4 peers | 33 |
| Observed IPv6 peers | 11 |
| IPv4 addresses originated | 18,432 |
| Observed IPv4 AS paths | 131,942 |
| Observed IPv6 AS paths | 52,938 |
| Average AS path length, all | 4.509 |
| Average AS path length, IPv4 | 4.409 |
| Average AS path length, IPv6 | 4.758 |

The HE page's counts changed during the research session: an earlier cached/search representation showed 153 originated prefixes (72 IPv4) and 27 peers, while the refreshed page showed 152 originated prefixes (71 IPv4) and 33 peers. Treat all these values as timestamped snapshots, not fixed inventory.

### 1.1 Reconciliation with bgp.tools and ipctl.io

Previously captured bgp.tools profile: 67 IPv4 and 68 IPv6 prefixes. The ipctl.io page loaded during this audit showed 139 total prefixes (71 IPv4, 68 IPv6), 135 Valid and 4 with no ROA; its page text also identifies 2026-10-16 as the underlying update date.

The arithmetic strongly suggests the count differences are caused by prefix-scope differences:

- 67 IPv4 Valid /24s plus 4 additional IPv4 aggregate announcements = 71 IPv4 originated.
- 68 IPv6 Valid routes plus 13 IPv6 Invalid /64 more-specifics = 81 IPv6 originated.
- 135 Valid + 13 Invalid + 4 IPv4 no-ROA routes = 152 originated.

This is a strong reconciliation hypothesis, not a substitute for comparing the raw prefix lists from each source. The 4 IPv4 no-ROA candidates are the aggregate routes discussed in section 4; confirm each directly with RIPEstat RPKI validation.

The HE page also reports 160 announced versus 152 originated: 8 additional IPv4 announcements are visible as carried/announced routes but are not counted as AS25145-originated routes. Identify the exact eight prefixes and their origin ASNs before making any topology or policy conclusion.

## 2. IPv6 RPKI-invalid routes reported by bgp.he.net

HE reports 13 RPKI-invalid IPv6 originated routes and 0 invalid IPv4 routes. The visible invalid IPv6 entries are:

| # | Prefix | Parent / context visible in HE |
|---:|---|---|
| 1 | 2a01:358:2000:13::/64 | Under 2a01:358::/29; prefix registrant is Türk Telekom, while HE lists AS25145 as announcing origin |
| 2 | 2a02:ac80:90::/64 | More-specific under the valid 2a02:ac80:90::/48 |
| 3 | 2a02:ac80:96::/64 | More-specific under the valid 2a02:ac80:96::/48 |
| 4 | 2a02:ac80:97::/64 | More-specific; parent entry found |
| 5 | 2a02:ac80:99::/64 | More-specific; parent entry found |
| 6 | 2a02:ac80:f1::/64 | More-specific under 2a02:ac80 |
| 7 | 2a02:ac80:100:1::/64 | More-specific under 2a02:ac80 |
| 8 | 2a02:ac80:105::/64 | More-specific under the valid 2a02:ac80:105::/48 |
| 9 | 2a02:ac80:127::/64 | More-specific; parent entry found |
| 10 | 2a02:ac81:101::/64 | More-specific under the valid 2a02:ac81:101::/48 |
| 11 | 2a02:ac81:102::/64 | More-specific under the valid 2a02:ac81:102::/48 |
| 12 | 2a02:ac87:0:2::/64 | More-specific under 2a02:ac87::/32 |
| 13 | 2a02:ac87:ac86::/64 | More-specific under 2a02:ac87::/32 |

Evidence examples:

- https://bgp.he.net/net/2a02:ac80:90::/64 shows origin AS25145, “IRR Match - Parent Entry Found”, and “ROA Signed and Invalid”.
- https://bgp.he.net/net/2a02:ac80:90::/48 shows origin AS25145 and both IRR and ROA Valid for the /48.
- https://bgp.he.net/net/2a01:358:2000:13::/64 shows origin AS25145, prefix registrant Türk Telekom, “IRR Invalid - Parent Route Origin Mismatch” and “ROA Signed and Invalid”.

**[UNVERIFIED ROOT CAUSE]** The 12 /64s under 2a02:ac80/ac81/ac87 may be invalid because the covering ROAs authorize only /48 or /32 lengths, or because the origin ASN does not match. The Türk Telekom-registered 2a01:358::/64 may be an origin-authorization mismatch. HE's badges do not expose the exact RIPE validator reason. Do not assume all 13 are invalid for the same reason.

Required validation for each prefix: query RIPEstat RPKI Validation with resource ASN 25145 and the exact prefix. The official endpoint distinguishes valid, invalid_asn, invalid_length and unknown. The result's description and covering ROA details must be retained.

## 3. Prefix-origin findings: AS25145 and AS51683

### 3.1 31.40.240.0/22

HE shows the aggregate 31.40.240.0/22 announced by AS25145. The four /24 delegations inside it are:

| Prefix | HE-observed origin | IRR / RPKI status shown by HE |
|---|---|---|
| 31.40.240.0/24 | AS25145 | IRR Valid, ROA Valid |
| 31.40.241.0/24 | AS51683 | IRR Valid, ROA Valid |
| 31.40.242.0/24 | AS51683 | IRR Valid, ROA Valid |
| 31.40.243.0/24 | AS51683 | IRR Valid, ROA Valid |

This is an aggregate-plus-more-specific arrangement: AS25145 originates the /22 aggregate, while AS51683 originates three /24s. If intentionally designed, the /24s win longest-prefix match where propagated. Validate the intended export and propagation policy at AS25145, AS51683, and each transit.

Sources:
- https://bgp.he.net/net/31.40.240.0/22
- https://bgp.he.net/net/31.40.241.0/24
- https://bgp.he.net/net/31.40.242.0/24
- https://bgp.he.net/net/31.40.243.0/24

### 3.2 185.115.208.0/22 address block

The HE page says 185.115.208.0/22 itself is **not visible in the global routing table**. Its allocations and observed more-specifics are:

| Prefix | HE observation |
|---|---|
| 185.115.208.0/24 | Origin AS25145; IRR Valid; ROA Valid |
| 185.115.209.0/24 | Origin AS51683; IRR Valid; ROA Valid |
| 185.115.210.0/23 | Not visible in the global routing table |
| 185.115.211.0/24 | Origin AS25145; IRR Valid; ROA Valid |

The 185.115.209.0/24 RIPE route object is origin AS51683, created 2025-01-03 and last modified 2025-01-03. It is not an AS25145-origin prefix; treat it as an AS51683 downstream/customer-origin route in inventory and monitoring.

Sources:
- https://bgp.he.net/net/185.115.208.0/22
- https://bgp.he.net/net/185.115.208.0/24
- https://bgp.he.net/net/185.115.209.0/24
- https://bgp.he.net/net/185.115.210.0/23
- https://bgp.he.net/net/185.115.211.0/24

### 3.3 Selected 77.92.96.0/19 routes

- 77.92.96.0/19 is announced by AS25145.
- 77.92.96.0/22 is also announced by AS25145; HE marks it “IRR Match - Parent Entry Found”.
- 77.92.96.0/24 and 77.92.106.0/24 are originated by AS25145 and shown IRR Valid / ROA Valid.
- 77.92.96.101 is covered by 77.92.96.0/24. HE's PTR listing for this address is server.imeys.com. PTR data is DNS evidence only; it does not establish asset ownership or current service health.

Sources:
- https://bgp.he.net/net/77.92.96.0/19
- https://bgp.he.net/net/77.92.96.0/22
- https://bgp.he.net/net/77.92.96.0/24
- https://bgp.he.net/net/77.92.106.0/24

### 3.4 213.144.96.0/19

HE shows 213.144.96.0/19 announced by AS25145 but labels its IRR state **“IRR Invalid - Origin Mismatch”**. The visible /24 more-specific entries in the AS25145 inventory are shown IRR Valid / ROA Valid. This aggregate-level mismatch needs a direct RIPE route-object and RPKI check; do not assume the valid child /24s make the /19 aggregate valid.

Source: https://bgp.he.net/net/213.144.96.0/19

## 4. AS51683 (Protahub) cross-check

Sources:
- https://bgp.he.net/AS51683
- https://bgpmap.net/as/51683
- https://bgp.tools/as/51683

HE's AS51683 page reports:

| Metric | Observation |
|---|---:|
| IPv4 originated | 5 |
| IPv6 originated | 1 |
| Total originated / announced | 6 |
| RPKI Valid | 6 |
| RPKI Invalid | 0 |
| Observed peers, all | 2 |
| Observed IPv4 peers | 2 |
| Observed IPv6 peers | 1 |
| Average AS path length, all | 5.333 |
| Average AS path length, IPv4 | 5.470 |
| Average AS path length, IPv6 | 4.882 |

The five IPv4 prefixes are 31.40.241.0/24, 31.40.242.0/24, 31.40.243.0/24, 185.9.138.0/24 and 185.115.209.0/24. The IPv6 prefix is 2a07:9d40::/48.

HE observes AS25145 and AS34984 as AS51683 IPv4 peers, and AS25145 as its IPv6 peer. bgpmap's RIS-derived page also lists AS25145 and AS34984 as observed upstreams.

The AS51683 RIPE aut-num declares imports from AS25145, AS34984 and AS15924, and exports AS51683 to all three. AS15924 is therefore present in the registry declaration but is not in the current HE observed peer list. This is a registry-vs-observed discrepancy, not proof that a live AS15924 session is down.

AS25145's RIPE aut-num declares import from AS51683 at preference 100 and export to AS51683 with announce ANY. AS51683's aut-num declares export to AS25145 announce AS51683. Compare these declarations with the live router policies and received/advertised route tables.

## 5. Third-party source disagreement and freshness

The ipctl.io AS25145 page loaded during this audit showed 139 announced prefixes (71 IPv4 and 68 IPv6), 135 Valid, 0 Invalid and 4 with no ROA. It also showed 97.9% IRR route-object coverage and 2 prefixes registered for another origin. Its page text dates the underlying data to 2026-10-16, so it is older than the HE page's 12 Nov 2026 update.

The ipctl.io page's observed-neighbour classification differs from HE and bgp.tools in places. For example, it classifies AS34984 among downstreams in its AS-path-derived view, while HE lists AS34984 as an IPv4 and IPv6 peer. These products use different data sources, sampling and relationship-classification methods. Do not turn a single dashboard's “upstream/downstream” label into a production topology fact.

The displayed ASPA expiry date also differed between ipctl crawl representations (2026-09-24 and 2026-10-22). As both dates are in the past relative to this audit, the current ASPA object and expiry must be queried directly from RIPE/RPKI before drawing a conclusion.

## 6. RIPEstat: what can be collected from the supplied Looking Glass links

The supplied RIPEstat pages are:

- https://stat.ripe.net/lg/185.115.209.0%2F24
- https://stat.ripe.net/lg/77.92.96.101
- https://stat.ripe.net/lg/77.92.106.0%2F24
- https://stat.ripe.net/lg/185.115.208.0%2F24

The interactive pages did not expose their route payload in this web extraction session. RIPE NCC documents the official Data API endpoints that provide the equivalent machine-readable evidence:

### 6.1 Looking Glass

Endpoint: https://stat.ripe.net/data/looking-glass/data.json

For a prefix or IP, RIPEstat returns collector/RRC locations and peer-level route data, including AS path, peer address, origin ASN, route prefix, next hop, communities, route last-updated time and latest confirmation time. Prefix queries must match a prefix present in routing data; IP queries resolve to the covering prefix.

### 6.2 Routing Status

Endpoint: https://stat.ripe.net/data/routing-status/data.json

Returns a routing-state summary for an ASN, IP or prefix. Historical queries are aligned to RIS collection points at 00:00, 08:00 and 16:00 UTC. The default minimum peer threshold is 10.

### 6.3 RPKI Validation

Endpoint: https://stat.ripe.net/data/rpki-validation/data.json

Requires an ASN resource and a prefix. The result distinguishes:
- valid
- invalid_asn
- invalid_length
- unknown

This is the required next check for the 13 IPv6 /64 routes and the four IPv4 aggregate candidates.

### 6.4 Example API requests

~~~bash
curl -fsS -G 'https://stat.ripe.net/data/looking-glass/data.json' \
  --data-urlencode 'resource=185.115.209.0/24' | jq .

curl -fsS -G 'https://stat.ripe.net/data/looking-glass/data.json' \
  --data-urlencode 'resource=77.92.96.101' | jq .

curl -fsS -G 'https://stat.ripe.net/data/routing-status/data.json' \
  --data-urlencode 'resource=77.92.106.0/24' | jq .

curl -fsS -G 'https://stat.ripe.net/data/rpki-validation/data.json' \
  --data-urlencode 'resource=25145' \
  --data-urlencode 'prefix=2a02:ac80:90::/64' | jq .
~~~

Official documentation:
- https://stat.ripe.net/docs/data-api/api-endpoints/looking-glass
- https://stat.ripe.net/docs/data-api/api-endpoints/routing-status.html
- https://stat.ripe.net/docs/data-api/api-endpoints/rpki-validation

Other useful RIPEstat endpoints for the next collection phase: announced-prefixes, asn-neighbours, asn-neighbours-history, bgp-updates, bgp-update-activity, bgplay, routing-history, visibility, prefix-overview and prefix-routing-consistency.

## 7. Priority follow-up checks

1. Run RIPEstat RPKI Validation for all 13 invalid IPv6 /64s. Record the exact invalid_asn versus invalid_length result, covering ROA, maxLength, validator time and origin ASN.
2. Validate the four IPv4 aggregate routes: 31.40.240.0/22, 77.92.96.0/19, 77.92.96.0/22 and 213.144.96.0/19. Confirm ROA state and IRR route-object origin.
3. Extract the eight IPv4 prefixes counted as announced but not originated by AS25145. Map each prefix to its origin ASN and downstream/customer.
4. Confirm whether the AS25145 aggregate-plus-customer-specific pattern for 31.40.240.0/22 is intentional and consistently propagated.
5. Confirm the intended announcement and RPKI/IRR state of 185.115.208.0/24, 185.115.209.0/24, 185.115.210.0/23 and 185.115.211.0/24.
6. Check AS51683's declared AS15924 relationship against current RIS peer visibility and the live BGP session state.
7. Query current AS25145 ASPA data and verify the published upstream provider list and expiry.
8. Capture RIPE RIS snapshots at regular intervals to detect prefix withdrawals, origin changes, AS-path changes, community changes and route flaps.

## 8. Evidence limitations

- Public route collectors do not show every router's Adj-RIB-In, Loc-RIB or Adj-RIB-Out.
- A route visible in a collector does not prove reachability from every network.
- A registry import/export policy is not proof of the live router policy.
- RPKI Invalid is not by itself proof of a hijack; it can result from origin or maxLength configuration errors.
- A PTR record is not an asset inventory or service-health check.
- No live router configuration, BGP session, route or production service was changed during this audit.

## Retrieval keywords

AS25145, AS-TEKNOTEL, AS51683, Protahub, bgp.he.net, RIPEstat, RIS, Looking Glass, BGP origin, AS_PATH, RPKI, ROA, invalid_length, invalid_asn, IRR, aggregate, more-specific, 31.40.240.0/22, 185.115.208.0/22, 185.115.209.0/24, 77.92.96.0/19, 77.92.106.0/24, 213.144.96.0/19, IPv6 /64, ASPA.
