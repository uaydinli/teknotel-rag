# Teknotel AS25145 BGP Communities, RTBH and Upstream Policy

Date recorded: 2026-11-13
Source: https://docs.t-cloud.com.tr/bgp-blackhole-nedir/
Related source: https://docs.t-cloud.com.tr/turkiye-de-hizmet-veren-isslere-ait-bgp-communities/
Evidence type: OBSERVED public documentation; no live router policy was inspected.
Status: Source captured and normalized for lexical RAG retrieval.

## 1. Scope and purpose

The source describes customer-facing BGP controls offered through Teknotel AS25145:

- BGP Blackhole / Remotely Triggered Black Hole (RTBH)
- Upstream-specific announcement suppression
- Generic and upstream-specific AS-path prepend
- Local Preference selection inside AS25145
- IPv4 and IPv6 operating guidance
- NOC validation and authorization boundaries

This is a policy reference, not proof that a particular customer BGP session currently accepts these communities.

## 2. Authorization and operational boundaries

| Control | Customer use | NOC use | Source qualification |
|---|---:|---:|---|
| 25145:666 RTBH | Yes | Yes | Controlled use |
| Generic prepend 25145:1001/1002/1003 | Yes | Yes | Traffic engineering |
| Upstream-specific no-advertise/prepend | Yes | Yes | Policy must be active on the relevant BGP session |
| Local Preference communities | Conditional | Yes | Changes route selection only inside AS25145 |
| Internal export-marking communities | No | Yes | Must not be exposed as customer action communities |
| Router/policy/show commands | No | Yes | NOC operations |
| DE-CIX route-server-specific policy details | No | Yes | NOC approval required |

## 3. General BGP and prefix rules

- Teknotel ASN: AS25145.
- Teknotel customer community namespace: 25145:xxxx.
- Customer router must send BGP communities (send-community).
- Recommended IPv4 RTBH prefix: /32.
- Recommended IPv6 RTBH prefix: /128.
- Normal IPv4 Internet announcement minimum is generally /24.
- Normal IPv6 announcement acceptance is determined by prefix policy; the source does not state one universal minimum length.
- Incorrect community or prefix use can cause service interruption, traffic loss, or reduced upstream redundancy.

## 4. Customer-facing base communities

| Community | Source-described behavior |
|---|---|
| 25145:444 | Suppress international announcements through Teknotel / national-only behavior |
| 25145:555 | International/transit announcement behavior; exact implementation is not specified in the source |
| 25145:666 | Blackhole / RTBH; traffic to the affected destination is dropped |
| 25145:1001 | Add 1 prepend to transit/upstream announcements |
| 25145:1002 | Add 2 prepends to transit/upstream announcements |
| 25145:1003 | Add 3 prepends to transit/upstream announcements |

The source states that the customer BGP session must accept the communities and the export policy must integrate them. Merely attaching a community at the customer router does not prove that Teknotel will apply the requested action.

## 5. RTBH behavior

### IPv4

- Recommended target: the attacked host as an exact /32.
- Community: 25145:666.
- Example from the source: 203.0.113.10/32 with 25145:666.
- /24 blackholing may work in some scenarios but can make the entire subnet unreachable; NOC approval and impact validation are required.

### IPv6

- Recommended target: the attacked IPv6 address as an exact /128.
- Community: 25145:666.
- Example from the source: 2a02:xxxx:xxxx::dead/128 with 25145:666.
- Do not use broad /48, /56, or /64 prefixes for routine IPv6 blackholing. Wider-prefix requests require separate approval because of service-impact risk.

### Operational consequence

Blackholing intentionally makes the target IP/prefix unreachable. It is a controlled, temporary mitigation for the attacked destination, not a method that preserves access to that destination.

## 6. Upstream-specific announcement suppression and prepend

These are Teknotel AS25145 communities that select an action toward the named upstream/peering relationship.

| Upstream / peering | ASN | Suppress announcement | 1 prepend | 2 prepends | 3 prepends | Source note |
|---|---:|---:|---:|---:|---:|---|
| Türk Telekom | AS9121 | 25145:2000 | 25145:2001 | 25145:2002 | 25145:2003 | Customer may request; NOC validates |
| Superonline | AS34984 | 25145:3000 | 25145:3001 | 25145:3002 | 25145:3003 | Customer may request; NOC validates |
| TiSparkle | AS6762 | 25145:4000 | 25145:4001 | 25145:4002 | 25145:4003 | Customer may request; NOC validates |
| Hurricane Electric | AS6939 | 25145:5000 | 25145:5001 | 25145:5002 | 25145:5003 | Customer may request; NOC validates |
| RETN | AS9002 | 25145:6000 | 25145:6001 | 25145:6002 | 25145:6003 | Customer may request; NOC validates |
| DE-CIX Istanbul / peering | AS20715 | 25145:8000 | 25145:8001 | 25145:8002 | 25145:8003 | NOC approval required |
| Voxility | AS3223 | 25145:9000 | 25145:9001 | 25145:9002 | 25145:9003 | May affect DDoS mitigation; NOC approval recommended |

The source requires the relevant peer policy to be active. It does not provide live evidence that every listed community is currently enabled on every customer session or upstream.

## 7. DE-CIX / route-server boundary

- DE-CIX Istanbul is described as a route-server/peering fabric, not a transit upstream.
- DE-CIX communities must not be treated as ordinary transit-provider communities.
- DE-CIX no-export/prepend actions require NOC approval.
- Route-server advertise communities and internal export marking are NOC operational controls.
- Customer requests for DE-CIX announcement suppression or prepend should be sent to the NOC.
- Preserve route-server advertise behavior; do not apply transit-style policy blindly.

## 8. Local Preference inside AS25145

The source explicitly limits these Local Preference actions to route selection inside Teknotel AS25145. They do not change the routing decisions of external upstream operators.

| Local Preference | Meaning |
|---:|---|
| 170 | Primary |
| 150 | Preferred |
| 90 | Backup |

Provider-specific customer/NOC community values:

| Provider | ASN | LP 170 | LP 150 | LP 90 |
|---|---:|---:|---:|---:|
| Türk Telekom | AS9121 | 25145:2090 | 25145:2091 | 25145:2092 |
| Superonline | AS34984 | 25145:3090 | 25145:3091 | 25145:3092 |
| TiSparkle | AS6762 | 25145:4090 | 25145:4091 | 25145:4092 |
| Hurricane Electric | AS6939 | 25145:5090 | 25145:5091 | 25145:5092 |
| RETN | AS9002 | 25145:6090 | 25145:6091 | 25145:6092 |

The source does not list Local Preference communities for DE-CIX AS20715 or Voxility AS3223. Their absence from this table is not proof that no internal policy exists.

For these communities to work, the corresponding customer-session import policy must be active.

## 9. Router configuration examples present in the source

The source includes examples for Juniper Junos IPv4 and IPv6, Cisco IOS/IOS-XE IPv4, and MikroTik RouterOS.

### Juniper Junos — IPv4

~~~text
set policy-options community TEKNOTEL-BLACKHOLE members 25145:666
set policy-options policy-statement EXPORT-TO-TEKNOTEL term BLACKHOLE from route-filter 203.0.113.10/32 exact
set policy-options policy-statement EXPORT-TO-TEKNOTEL term BLACKHOLE then community add TEKNOTEL-BLACKHOLE
set policy-options policy-statement EXPORT-TO-TEKNOTEL term BLACKHOLE then accept
set protocols bgp group TEKNOTEL export EXPORT-TO-TEKNOTEL
~~~

### Juniper Junos — IPv6

~~~text
set policy-options community TEKNOTEL-BLACKHOLE members 25145:666
set policy-options policy-statement EXPORT-TO-TEKNOTEL-V6 term BLACKHOLE-V6 from route-filter 2a02:xxxx:xxxx::dead/128 exact
set policy-options policy-statement EXPORT-TO-TEKNOTEL-V6 term BLACKHOLE-V6 then community add TEKNOTEL-BLACKHOLE
set policy-options policy-statement EXPORT-TO-TEKNOTEL-V6 term BLACKHOLE-V6 then accept
set protocols bgp group TEKNOTEL-V6 export EXPORT-TO-TEKNOTEL-V6
~~~

### Cisco IOS / IOS-XE — IPv4

~~~text
ip prefix-list BLACKHOLE-IP seq 10 permit 203.0.113.10/32

route-map EXPORT-TO-TEKNOTEL permit 10
 match ip address prefix-list BLACKHOLE-IP
 set community 25145:666 additive

router bgp <CUSTOMER_ASN>
 neighbor <TEKNOTEL_PEER_IP> send-community
 neighbor <TEKNOTEL_PEER_IP> route-map EXPORT-TO-TEKNOTEL out
~~~

### MikroTik RouterOS

~~~text
/routing filter rule
add chain=bgp-out rule="if (dst == 203.0.113.10/32) { append bgp-communities 25145:666; accept; }"
~~~

The source warns that examples vary by vendor/version and requires checking the customer BGP session, prefix policy, and send-community before implementation. The Junos snippets show an export-policy attachment; they must be integrated with the customer's existing export policy rather than copied blindly into a live router. This last sentence is an operational safety inference, not a statement made by the source.

## 10. Distinction from upstream-native communities

The related T-Cloud article “Türkiye'de hizmet veren ISS'lere ait BGP communities” documents communities in upstream ASN namespaces, for example:

- 34984:666 for Superonline blackhole.
- 6762:666 for Sparkle blackhole.
- 3223:666 for Voxility blackhole.
- 9121:444 / 9121:666 for Türk Telekom announcement/blackhole behavior.

These are not the same namespace as the customer-facing Teknotel communities 25145:xxxx.

Interpretation:
- 25145:666 is sent by a customer toward Teknotel AS25145 to request Teknotel's RTBH action.
- 34984:666, 6762:666, 3223:666, and 9121:... belong to upstream ASN policy namespaces described by the separate upstream-community reference.
- Do not substitute one namespace for the other without confirming the exact BGP policy point and provider requirements.

The two public documents describe different policy domains; this distinction is an interpretation based on their respective ASN/community namespaces.

## 11. Evidence limits / not verified

The inspected source does not establish:

- That any listed community is currently accepted on a specific customer BGP session.
- That all upstream-specific actions are enabled on every Teknotel edge or peer.
- The exact route-map/policy implementation, policy order, or community propagation behavior in production.
- Whether IPv4 and IPv6 policy activation is identical on every peer.
- Any live RTBH test result, route acceptance output, RIB/FIB state, or traffic-drop measurement.
- Vendor software versions for the customer configuration examples.
- The exact behavior of 25145:555 beyond the source's “international/transit announcement behavior” description.

No live router configuration, BGP session, route, or traffic was changed or tested during this review.

## 12. Retrieval keywords

AS25145, BGP community, BGP communities, RTBH, remote triggered black hole, blackhole, 25145:666, 25145:444, 25145:555, 25145:1001, 25145:1002, 25145:1003, AS9121, AS34984, AS6762, AS6939, AS9002, AS20715, AS3223, DE-CIX, Voxility, TiSparkle, RETN, Hurricane Electric, Local Preference, AS-path prepend, Junos, IOS-XE, RouterOS.
