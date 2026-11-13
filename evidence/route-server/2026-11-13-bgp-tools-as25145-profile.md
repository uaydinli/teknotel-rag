# AS25145 — bgp.tools ASN Profile and Routing Policy Review

**Captured:** 2026-11-13  
**Primary source:** https://bgp.tools/as/25145  
**Community source:** https://bgp.tools/communities/25145  
**Source freshness shown by bgp.tools:** ASN page last update 2026-11-11T03:23:53Z; DE-CIX IX data last update 2026-11-12T10:08:17Z.  
**Evidence class:** Public BGP.tools page and embedded RIPE aut-num/IRR policy text.  
**Important:** This is public routing/registry evidence. It is not a live router configuration export, session-state check, or proof that every declared policy is implemented.

## 1. AS identity and role

| Field | Value |
|---|---|
| ASN | AS25145 |
| AS name / AS-SET | AS-TEKNOTEL |
| Organization | Teknotel Telekomunikasyon Sanayi Ve Ticaret A.S. |
| Also known as | Telehouse Istanbul |
| RIPE registration date | 2002-08-07 |
| Network status | Active, allocated under RIPE |
| bgp.tools network type | Eyeball |
| Declared services | Residential Broadband ISP, Enterprise ISP, IP Transit Provider, Carrier Neutral Datacenter, Hosting and Cloud Provider |
| Routing-security declarations | MANRS Network Operator Participant; RPKI ROV Enabled; RPKI ROA Valid |
| PeeringDB AS-SET | RIPE::AS-TEKNOTEL |
| Looking Glass | https://lg.teknotel.com/ |
| NOC contact shown in aut-num | noc@teknotel.com |
| Abuse contact shown in aut-num | abuse@teknotel.com |

The “Eyeball” classification and rankings are bgp.tools classifications, not a formal service taxonomy.

## 2. Originated prefix inventory

bgp.tools reports **67 IPv4 and 68 IPv6 originated prefixes**.

### IPv4

The page reports 67 IPv4 /24s. The listed ranges can be summarized as:

| Prefix group | Visible origin entries | Count |
|---|---|---:|
| 31.40.240.0/24 | 31.40.240.0/24 | 1 |
| 77.92.96.0/19 | 77.92.96.0/24 through 77.92.127.0/24 | 32 |
| 185.115.208.0/24 | 185.115.208.0/24 | 1 |
| 185.115.211.0/24 | 185.115.211.0/24 | 1 |
| 185.231.108.0/24 | 185.231.108.0/24 | 1 |
| 213.144.96.0/19 | 213.144.96.0/24 through 213.144.127.0/24, except 213.144.102.0/24 | 31 |
| **Total** |  | **67** |

The page displays a valid-RPKI indicator beside the listed IPv4 prefixes. This is the status shown by bgp.tools at capture time; it is not a substitute for checking current ROA origin ASN, maxLength, and validator state independently.

### IPv6

The page reports 68 IPv6 prefixes. The visible inventory includes:

- Multiple /48s within the 2a02:ac80:: address space.
- 2a02:ac81::/32, 2a02:ac82::/32, 2a02:ac83::/32, 2a02:ac84::/32, 2a02:ac85::/32, 2a02:ac86::/32, and 2a02:ac87::/32.
- Additional more-specific /48 entries under 2a02:ac81 and 2a02:ac87.

The page also reports **458,808 /48-equivalents of IPv6 address space**. Do not interpret this number as 458,808 separately announced BGP prefixes; the page separately reports 68 IPv6 prefix entries.

The displayed IPv6 prefix rows also carry valid-RPKI indicators.

### Prefix-limit observation

bgp.tools “Suggested Prefix Limits” shows:

- IPv4: 67
- IPv6: 63

This differs from the page's originated-prefix count of 68 IPv6. This is a source-side count discrepancy that should be reconciled before using the suggested IPv6 limit as a production maximum-prefix value. Do not blindly configure 63.

## 3. Observed topology in bgp.tools

At the captured page version:

| Relationship | Count |
|---|---:|
| Peers | 35 |
| Upstreams | 8 |
| Direct downstreams | 5 |
| AS cone | 13 |

The page states that network-policy graph data may take up to two hours to update. It also displays a “Not Connected To realtime data updates” indicator. Treat these counts as a timestamped public observation, not a real-time NOC dashboard.

### Upstreams listed by the current topology table

| ASN | Network | IPv4 | IPv6 |
|---|---|---:|---:|
| AS9121 | Türk Telekom | Yes | Yes |
| AS6762 | Telecom Italia Sparkle / Seabone | Yes | Yes |
| AS6939 | Hurricane Electric | Yes | Yes |
| AS15924 | Vodafone Turkey | Yes | Yes |
| AS34984 | Superonline | Yes | Yes |
| AS9002 | RETN | Yes | Yes |
| AS3223 | Voxility | Yes | No |
| AS39582 | Vaultr | Yes | Yes |

### Important peers visible in the table

The peer list includes the upstreams above and networks such as:

- AS51683 Protahub
- AS16740 DOXX.NET
- AS13335 Cloudflare
- AS8075 Microsoft
- AS40934 Fortinet
- AS25091 IP-Max
- AS43009 Infobip
- AS51095 EdgeUno
- AS47524 Türksat
- AS6823 3C1B
- AS199524 Gcore
- AS208972 GIBIRNet
- AS201178 Euronet
- AS19551 Incapsula
- AS139341 WeChat/QQ CDN
- AS6663 Türk Telekom International
- AS206375 NETSPEED
- AS202294 Netlojik
- AS21859 Zenlayer
- AS136907 Huawei Cloud
- AS21245 Medianova
- AS32934 Facebook
- AS6507 Riot Games
- AS212066 Yandex Turkey
- AS42 WoodyNet

The table's IPv4/IPv6 check marks are peer-family observations, not proof of equal traffic volume, bandwidth, or service quality. For example, Voxility is shown with IPv4 but no IPv6 on this page.

### Direct downstreams

| ASN | Network | IPv4 | IPv6 |
|---|---|---:|---:|
| AS51683 | Protahub | Yes | Yes |
| AS16740 | DOXX.NET | Yes | Yes |
| AS40934 | Fortinet | Yes | No |
| AS43009 | Infobip | Yes | No |
| AS15924 | Vodafone Turkey | No | Yes |

AS15924 appears in both the upstream and downstream tables, with different address-family flags in the downstream entry. Preserve this as an observed topology classification; do not infer a commercial relationship or a routing fault from the label alone.

## 4. DE-CIX Istanbul IXP record

bgp.tools lists one Internet Exchange Point:

| Field | Value |
|---|---|
| IXP | DE-CIX Istanbul |
| IPv4 peering address | 185.1.48.51 |
| IPv6 peering address | 2001:7f8:3f::6239:0:1 |
| Listed link speed | 30 Gbps |
| Detected vendor | Juniper Networks |
| IXP data timestamp | 2026-11-12T10:08:17Z |

The 30 Gbps value is the link-speed value displayed by bgp.tools. It does not prove current utilization, available headroom, physical port aggregation, or end-to-end capacity.

## 5. RIPE aut-num import policy shown by bgp.tools

The embedded AS25145 aut-num contains these import declarations:

| Neighbor ASN | Name | Declared preference | Declared import |
|---|---|---:|---|
| AS9121 | Türk Telekom | 170 | ANY |
| AS47123 | TI Sparkle Turkey | 150 | ANY |
| AS34984 | Superonline | 170 | ANY |
| AS15924 | Vodafone Turkey | 170 | ANY |
| AS6762 | Telecom Italia Sparkle | 160 | ANY |
| AS6939 | Hurricane Electric | 160 | ANY |
| AS9002 | RETN | 160 | ANY |
| AS39582 | Vaultr | 150 | ANY |
| AS3223 | Voxility | 150 | ANY |
| AS43009 | Infobip | 100 | AS43009 |
| AS57419 | Customer ASN | 100 | AS57419 |
| AS51683 | Protahub | 100 | AS51683 |
| AS59886 | Customer ASN | 100 | AS59886 |
| AS40934 | Fortinet | 100 | AS40934 |
| AS214381 | Customer ASN | 100 | AS214381 |

These are RIPE IRR/RPSL declarations. ANY in the registry object is not proof that the production router has no inbound prefix filtering. Verify actual import policy and received routes on the relevant routers.

### IRR preference observations

- AS9121 and AS34984 are declared at preference 170.
- AS6762, AS6939, and AS9002 are declared at preference 160.
- AS39582 and AS3223 are declared at preference 150.
- Customer imports shown are declared at preference 100.
- AS47123 appears in the RIPE import policy at preference 150, but is absent from the current eight-member upstream list in the bgp.tools topology table.

The AS47123 difference is a registry-vs-observed-topology discrepancy. It may be a stale or non-current IRR declaration; this page alone cannot establish whether a live session exists.

## 6. RIPE aut-num export policy shown by bgp.tools

The visible export declarations are:

- To AS9121, AS34984, AS15924, AS6762, AS6939, AS9002, AS39582, AS3223, and AS47123: announce AS25145:AS-CUSTOMERS.
- To AS214381: announce AS25145:AS-CUSTOMERS.
- To AS15924, AS40934, AS43009, AS57419, AS51683, and AS59886: announce ANY.

AS15924 has both an announce ANY line and an announce AS25145:AS-CUSTOMERS line. This is a broad/overlapping declaration in the published aut-num. Confirm intended policy with the IRR maintainer and compare it with the actual router export policy.

ANY and AS-SET references in RPSL describe declared routing policy. They do not by themselves prove what a router is currently advertising.

## 7. Routing security and AS-SET references

The aut-num remarks identify:

- MANRS Network Operator Participant.
- RPKI ROV Enabled.
- RPKI ROA Valid.
- AS-SET AS-TEKNOTEL.
- Customer set AS25145:AS-CUSTOMERS.
- Upstream set AS25145:AS-UPSTREAMS.

The page lists membership in multiple RIPE/RADB/LEVEL3 AS-SETs, including as25145:as-upstreams, as-teknotel, as-turktelekom, as-ttnet, as-sparkle-tr, RETN IPv4/IPv6 sets, Hurricane IPv4/IPv6 sets, and DE-CIX Istanbul route-server/connected sets.

PeeringDB AS-SET is RIPE::AS-TEKNOTEL.

## 8. Cross-check with the separate T-Cloud / bgp.tools community reference

The bgp.tools community page lists these additional base communities:

| Community | bgp.tools description |
|---|---|
| 25145:444 | Do not announce internationally via Teknotel; also applies to 9121:444 and 34984:444; minimum /24 |
| 25145:666 | Blackhole via Teknotel; valid for /32 and /24 |
| 25145:1001 | One prepend to transit providers; minimum /24 |
| 25145:1002 | Two prepends to transit providers; minimum /24 |
| 25145:1003 | Three prepends to transit providers; minimum /24 |
| 25145:1090 | Set route as backup, Local Preference 90; minimum /24 |
| 25145:1050 | Set route as peering, Local Preference 150; minimum /24 |
| 25145:1070 | Set route as directly connected, Local Preference 170; minimum /24 |

Provider-specific controls in the page:

| Provider | ASN | No announce | Prepend 1/2/3 |
|---|---:|---:|---|
| Türk Telekom | 9121 | 25145:2000 | 2001 / 2002 / 2003 |
| Superonline | 34984 | 25145:3000 | 3001 / 3002 / 3003 |
| TI Sparkle | 6762 | 25145:4000 | 4001 / 4002 / 4003 |
| Hurricane Electric | 6939 | 25145:5000 | 5001 / 5002 / 5003 |
| RETN | 9002 | 25145:6000 | 6001 / 6002 / 6003 |
| DE-CIX Istanbul | 20715 | 25145:8000 | 8001 / 8002 / 8003 |
| Voxility | 3223 | 25145:9000 | 9001 / 9002 / 9003 |

Voxility-specific additional communities:

- 25145:9012: announce via Voxility toward AS6762 TI Sparkle.
- 25145:9013: announce via Voxility toward AS6939 Hurricane Electric.
- 25145:9014: announce via Voxility toward AS9002 RETN.
- 25145:9000 is explicitly warned to potentially disable DDoS protection.

Provider-specific Local Preference communities listed:

| Provider | LP 170 | LP 150 | LP 90 |
|---|---:|---:|---:|
| AS9121 | 25145:2090 | 25145:2091 | 25145:2092 |
| AS34984 | 25145:3090 | 25145:3091 | 25145:3092 |
| AS6762 | 25145:4090 | 25145:4091 | 25145:4092 |
| AS6939 | 25145:5090 | 25145:5091 | 25145:5092 |
| AS9002 | 25145:6090 | 25145:6091 | 25145:6092 |

### Differences from the T-Cloud BGP Blackhole guide

The T-Cloud guide previously captured in this repository documents 25145:555, while the bgp.tools known-community page does not list it. Conversely, bgp.tools lists 25145:1050, 25145:1070, 25145:1090, and 25145:9012/9013/9014, which are not included in that T-Cloud guide's community table.

The T-Cloud guide describes IPv6 RTBH using /128; the bgp.tools community page only explicitly states /32 and /24 for 25145:666, and does not confirm /128 acceptance.

Treat these as source-scope/version differences requiring NOC confirmation. Do not infer that an omitted community is invalid or that a listed community is enabled on every customer session.

## 9. Cross-check with the T-FortiFirewall-ANK audit

The separate FortiGate-100F audit records these IPv4 ISP peers:

- AS34984 Superonline.
- AS39582 Vaultr.

Both ASNs appear in the current bgp.tools upstream table and RIPE import declarations. The FortiGate audit also records AS51683 ProtaHub as a downstream/customer peer; AS51683 appears in the bgp.tools peer and downstream tables.

The FortiGate audit records route-map Prepend setting community 25145:1006. Neither the bgp.tools known-community page nor the captured T-Cloud community guide defines 25145:1006. Its meaning remains NOT VERIFIED. Do not treat it as equivalent to 25145:1001/1002/1003 or any upstream-specific action community without NOC confirmation.

Related audit: https://github.com/uaydinli/datacenter/blob/main/docs/fortigate-ank-bgp-audit.md

## 10. Findings and follow-up checks

1. Prefix inventory: reconcile 67 IPv4 /24s and 68 IPv6 prefix entries with the authoritative prefix inventory, ROAs, IRR route objects, and actual advertisements.
2. IPv6 prefix limit: investigate why suggested IPv6 max-prefix is 63 while 68 originated IPv6 prefixes are listed. Do not copy 63 into production without confirming the expected received prefix count at each peer.
3. AS47123: verify whether the RIPE import/export declaration is still intended; it is present in the aut-num but absent from the current eight-upstream topology table.
4. AS15924: it is classified as both upstream and downstream; downstream row is IPv6-only. Confirm whether this is an intentional asymmetric AFI/relationship arrangement.
5. IRR export to AS15924: the aut-num contains both announce ANY and announce AS25145:AS-CUSTOMERS; verify the intended export policy.
6. Community coverage: confirm current acceptance and behavior of 25145:555, 25145:1050/1070/1090, 25145:9012/9013/9014, and 25145:1006 with the NOC.
7. RTBH AFI: confirm whether 25145:666 is accepted for IPv6 /128; bgp.tools page does not state this, while the T-Cloud guide does.
8. Voxility: treat 25145:9000 as high-impact because the community description warns that DDoS protection may be disabled. Validate route impact and mitigation path before any use.
9. DE-CIX: confirm the 30 Gbps IXP link record against PeeringDB/DE-CIX port details and live interface inventory; bgp.tools alone does not prove current capacity or utilization.
10. RPKI: independently validate ROA origin ASN and maxLength for every announced prefix and confirm live ROV policy; the page's valid icons are only a snapshot.

## 11. Evidence limits

This review does not prove:

- Current BGP session state or uptime.
- Current received/advertised route counts on any individual router.
- Live router import/export policy, route-map order, or community propagation.
- Traffic volume, utilization, latency, loss, or physical link diversity.
- Actual Voxility DDoS mitigation state.
- Current acceptance of every community on every customer session.
- That RIPE ANY declarations are implemented literally in production.
- That every originated prefix is currently reachable from every global vantage point.

No live router configuration or production route was changed during this review.

## 12. Retrieval keywords

AS25145, AS-TEKNOTEL, Teknotel, Telehouse Istanbul, bgp.tools, RIPE aut-num, IRR, AS25145:AS-CUSTOMERS, AS25145:AS-UPSTREAMS, AS9121, AS47123, AS34984, AS15924, AS6762, AS6939, AS9002, AS39582, AS3223, AS51683, AS16740, AS40934, AS43009, DE-CIX Istanbul, RPKI, ROV, ROA, MANRS, IPv4 prefixes, IPv6 prefixes, prefix-limit, Local Preference, RTBH, 25145:666, 25145:9000, 25145:9012, 25145:9013, 25145:9014.
