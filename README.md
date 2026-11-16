# Teknotel RAG

Persistent technical knowledge and evidence repository for Teknotel infrastructure, RAG, Graylog, FortiDDoS and related network/debugging work.

## Evidence-first workflow
This repository is the persistent project record. In this ChatGPT conversation, every meaningful discovery, debugging result, configuration finding, packet-analysis finding, command output, hypothesis change, and verified conclusion should be recorded here without waiting for a separate GitHub-update request.

## Evidence rules
- Record observations separately from hypotheses and conclusions.
- Never fabricate missing command output or inferred configuration.
- Preserve raw evidence when available; add an interpreted summary alongside it.
- Include date/time, system/component, command or source, and result.
- For packet captures, record the file name and analysis scope and preserve derived findings.
- For configuration changes, record what changed, why, and the verification result.
- Prefer append-only evidence logs for investigations.
- Never commit secrets, credentials, private keys or authentication tokens.

## BGP / Route Server references
- [DE-CIX Istanbul AS25145 / TurkNet AS12735 IPv4+IPv6 peering investigation](evidence/route-server/2026-11-16-de-cix-turknet-as12735-bgp-peering.md) — committed peer configuration, dedicated IPv6 export policy, Connect/ConnectRetry states, prior TCP SYN_SENT observations, empty route exchange, evidence/inference separation and TurkNet NOC follow-up.
- [Teknotel AS25145 BGP communities, RTBH and upstream policy](evidence/route-server/2026-11-13-tcloud-bgp-blackhole-communities.md) — customer-facing RTBH, upstream announcement suppression/prepend, Local Preference and NOC boundaries.
- [AS25145 bgp.tools ASN profile and routing policy review](evidence/route-server/2026-11-13-bgp-tools-as25145-profile.md) — originated IPv4/IPv6 prefixes, upstreams, peers, downstreams, DE-CIX, RIPE import/export policy, RPKI, community discrepancies and validation items.
- [AS25145 bgp.he.net + RIPEstat expanded BGP audit](evidence/route-server/2026-11-13-bgp-he-ripestat-as25145-expanded-audit.md) — 13 IPv6 RPKI-invalid /64s, AS51683 customer-origin routes, aggregate/more-specific mapping, prefix-count reconciliation and RIPEstat API collection plan.

## Current Graylog investigation
The discovery scope is: stream rules, pipeline definitions, pipeline-to-stream bindings, pipeline rules, index sets, and index ranges.
The exact MongoDB command output is not present in the current repository context, so no unverified values are recorded.
