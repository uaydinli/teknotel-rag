# DE-CIX Istanbul — AS25145 / AS12735 TurkNet BGP Peering Investigation

**Captured:** 2026-11-16  
**Device:** C07-MX304-R2  
**Junos:** 23.4R2-S2.1  
**Routing context:** master  
**Evidence class:** User-provided live Junos command output and configuration transcript.  
**Status:** Both address-family sessions remain in Connect; TCP handshake is not completing in the captured diagnostics.

## 1. Peering endpoints

| Field | IPv4 | IPv6 |
|---|---|---|
| Local ASN | AS25145 | AS25145 |
| Local address | 185.1.48.51 | 2001:7f8:3f::6239:0:1 |
| Remote ASN | AS12735 | AS12735 |
| Remote address | 185.1.48.12 | 2001:7f8:3f::31bf:0:1 |
| Group | turknet | turknet |
| Export policy | turknet-out | turknet-out-v6 |
| Import policies | BGP-BOGON-IN-V4, turknet-aspath-check, turknet-rpki-in | turknet-aspath-check, turknet-rpki-in |

## 2. Configuration recorded

The peer configuration was committed successfully on re0 and re1 (commit complete).

### AS_PATH validation

Configured expression:

~~~junos
set policy-options as-path TURKNET-AS12735 ".* 12735 .*"
~~~

Import policy behavior:
- ACCEPT-AS12735 matches BGP routes whose AS_PATH contains AS12735 and uses then next policy.
- REJECT-OTHER rejects routes that do not match.
- Matching routes continue to turknet-rpki-in.

**Interpretation:** The configured expression checks that AS12735 occurs somewhere in the AS_PATH. It does not enforce AS12735 as the first AS in the path.

### RPKI import policy

The configured turknet-rpki-in policy:
- Rejects validation-state invalid.
- Sets local preference 170 and accepts unknown.
- Sets local preference 170 and accepts valid.

IPv4 also applies BGP-BOGON-IN-V4; this is an IPv4-only bogon policy and is not attached to the IPv6 neighbor in the captured configuration.

### Export policies

IPv4 turknet-out:
- Accepts prefixes in Teknotel-Dist.
- Rejects everything else.

IPv6 turknet-out-v6:
- Accepts prefixes in route-filter-list Teknotel_Dist_IPV6.
- Rejects everything else.

The IPv6 neighbor was changed from Teknotel_Dist_IPV6 to the dedicated turknet-out-v6 policy and the change was committed. This avoids applying the existing DE-CIX-specific community actions in Teknotel_Dist_IPV6 (including CS_DECIX_ADVERTISE_TO_ALL_PEERS and UPSTREAM-DECIX) to TurkNet.

IPv6 prefix limit:
- Maximum: 1000
- Teardown threshold: 80%
- Idle timeout: 1 minute

## 3. Live BGP observations

### BGP summary

Captured summary reports:
- 63 groups, 71 peers, 9 down peers.
- IPv4 peer 185.1.48.12, AS12735: InPkt 0, OutPkt 0, state Connect; displayed uptime/down timer 7:33.
- IPv6 peer 2001:7f8:3f::31bf:0:1, AS12735: InPkt 0, OutPkt 0, state Connect; displayed uptime/down timer 7:33.
- Existing TurkSat peers remain Established:
  - 185.1.48.62, AS47524.
  - 2001:7f8:3f::b9a4:0:1, AS47524.

### Neighbor detail

Both neighbors report:
- State: Connect.
- Last State: Connect.
- Last Event: ConnectRetry.
- Last Error: None.
- Number of flaps: 0.

IPv6 neighbor additionally reports flag TryConnect.

Configured export/import policies are shown in the neighbor detail and match the policies listed above.

### TCP state

A preceding show system connections capture showed:

~~~text
tcp4  185.1.48.51.60349  -> 185.1.48.12.179                 SYN_SENT
tcp6  2001:7f8:3f::6239:0:1.50213 -> 2001:7f8:3f::31bf:0:1.179 SYN_SENT
~~~

This indicates that the local router had sent TCP connection attempts but had not completed the TCP handshake in that capture.

### Route exchange

The captured commands:
- show route receive-protocol bgp 185.1.48.12
- show route receive-protocol bgp 2001:7f8:3f::31bf:0:1
- show route advertising-protocol bgp 185.1.48.12
- show route advertising-protocol bgp 2001:7f8:3f::31bf:0:1

show no peer-specific received or advertised route entries. This is consistent with sessions not being Established.

### Logs and reachability

- The supplied show log messages matches for both peer addresses returned no lines in the captured output.
- Earlier troubleshooting reported successful ICMP ping to both peer addresses. ICMP reachability does not prove TCP/179 reachability.

## 4. Findings — evidence versus interpretation

### OBSERVED

1. Both IPv4 and IPv6 BGP sessions are in Connect.
2. Both neighbors report ConnectRetry and Last Error None.
3. Both peers have zero BGP packets in the supplied summary.
4. TCP connections were observed in SYN_SENT in the preceding diagnostic capture.
5. No peer routes are shown as received or advertised.
6. Existing TurkSat IPv4 and IPv6 sessions are Established.
7. Dedicated IPv6 export policy turknet-out-v6 is configured and committed.
8. No matching log messages were present in the supplied output.

### INFERRED

The BGP FSM has not reached the OPEN-message exchange. The import/export policy contents, AS_PATH matching, and RPKI validation are not yet the cause demonstrated by this evidence because no BGP session has been established to exchange UPDATE messages.

### HYPOTHESIS — NOT VERIFIED

Possible causes include:
- TurkNet has not yet provisioned or enabled one or both BGP neighbors.
- Remote-side TCP/179 ACL or firewall filtering.
- Remote-side source/destination address or ASN mismatch.
- A peering/VLAN-side filtering or activation issue specific to this peer.

The supplied evidence cannot distinguish these possibilities. The fact that both AFI sessions fail similarly makes a common remote-side provisioning or TCP reachability issue plausible, but it is not proof.

## 5. NOC follow-up

Ask TurkNet NOC to verify:
1. IPv4 neighbor 185.1.48.51 with remote AS25145.
2. IPv6 neighbor 2001:7f8:3f::6239:0:1 with remote AS25145.
3. Both BGP neighbors are administratively enabled.
4. TCP/179 is permitted in both directions.
5. DE-CIX peering/VLAN activation and any peer-specific ACLs.
6. Their local BGP state and logs for both sessions.

Do not make additional local BGP policy changes solely to address the current Connect/SYN_SENT state. Recheck session state after TurkNet confirms provisioning.

## 6. Post-establishment validation

After both sessions become Established:
- Verify received routes and accepted counts.
- Verify AS_PATH rejects routes that do not contain AS12735.
- Verify RPKI-invalid routes are rejected.
- Verify only Teknotel-Dist IPv4 and Teknotel_Dist_IPV6 IPv6 prefixes are advertised.
- Verify the IPv6 export does not carry DE-CIX-specific communities.
- Review IPv6 bogon filtering separately; no IPv6 bogon policy is evidenced in the captured configuration.

## 7. Retrieval keywords

AS25145, AS12735, TurkNet, DE-CIX Istanbul, C07-MX304-R2, Juniper MX304, Junos 23.4R2-S2.1, 185.1.48.12, 185.1.48.51, 2001:7f8:3f::31bf:0:1, 2001:7f8:3f::6239:0:1, BGP Connect, ConnectRetry, SYN_SENT, TCP/179, AS_PATH, RPKI, turknet-aspath-check, turknet-rpki-in, turknet-out, turknet-out-v6, Teknotel-Dist, Teknotel_Dist_IPV6, DE-CIX communities.
