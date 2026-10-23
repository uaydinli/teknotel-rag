# Route Server GoBGP — FlowSpec, policy and service log discovery

Date: 2026-10-23
Source: Operator-provided CLI output on rs; sanitized for public repository
Status: read-only evidence

## OBSERVED
- `gobgp global rib summary -a ipv4-flowspec`: AFI_IP / SAFI_FLOW_SPEC_UNICAST; Destination 0, Path 0.
- Configuration grep for policy, apply-policy, defined-sets, prefix-set, as-path-set, community-set or flowspec showed only the two configured `ipv4-flowspec` AFI/SAFI entries. No matching policy definition or assignment in this TOML.
- Journal (Oct 20 12:59:43 UTC and Oct 21 15:34:56 UTC): `the received Update message was treated as withdraw`, `unknown evpn subtype: 249`, attributed to peer A (private address omitted).
- Journal (Oct 20 14:22:10 UTC): process PID 1140 logged `sent notification` to peer A, Code 6, Subcode 3, State BGP_FSM_ESTABLISHED.
- Current process PID 1444; elapsed 2d 22:57:35, ps CPU 8.6%, memory 17.6%, RSS 2889048 KiB.

## INTERPRETATION AND LIMITS
- IPv4 FlowSpec was negotiated by both peers in earlier discovery but the *global* FlowSpec RIB currently has zero entries; this does not establish whether FlowSpec was previously used or whether peers carry routes in separate tables.
- Journal notification from old PID 1140 is not the same observation as the current peer A counter showing 53 **received** notifications. Do not conflate directions or process lifetimes.
- `unknown evpn subtype: 249` is evidence of parsing a received update as withdraw; no causal relation to FlowSpec or advertised route counts is demonstrated.
- Exact cause for zero advertised routes remains UNVERIFIED. No operational changes authorized.

## NEXT READ-ONLY CHECKS
- Examine systemd unit and sanitized daemon configuration startup flags / log behavior.
- Review targeted recent BGP FSM events with timestamps without dumping full journal.
- Inspect GoBGP local and neighbor policy assignment with version-appropriate documented command/API.
- Confirm intended Route Server behavior and expected peer-to-peer route advertisement before proposing any policy change.
