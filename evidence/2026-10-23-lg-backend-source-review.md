# Looking Glass backend source review — 2026-10-23

Evidence source: operator-supplied excerpts of application main module and BGP RPC client.
Review scope: static code inspection. No live exploit tests; no application change.

## OBSERVED
- Diagnostic endpoints invoke ping and tracepath via subprocess argument arrays with timeouts. No shell=True in reviewed code.
- Target validation checks length and hostname-like character syntax; no explicit restriction on private, loopback or link-local destinations.
- Ping returns process stdout and stderr without redaction. Tracepath applies a finite IPv4-oriented regex redactor.
- Route lookup trims prefix and limits length but does not perform CIDR validation before passing it to the BGP client.
- The BGP client connects to a remote service via grpc.insecure_channel (no transport encryption configured in this client).
- Global and peer table lookups use streaming RPCs with 5-second deadlines. Peer listing also uses a 5-second deadline.
- API mounts a static directory and includes a separate Atlas router module.
- No explicit auth or rate-limiting middleware appears in the two reviewed modules. Upstream Cloudflare controls have not been inspected.

## RISKS / UNVERIFIED
- Internal-network probing could be possible if the endpoint is publicly accessible without upstream authorization. Public reachability is not yet verified.
- Returned diagnostic output may reveal network internals. Masking completeness is unverified.
- Exposure and authentication of the remote BGP gRPC listener are not established; insecure_channel alone does not prove public exposure.
- Atlas request authorization, DNS input normalization, frontend protections and production middleware require inspection of other files.

## RECOMMENDED NEXT EVIDENCE
- Read-only review of Cloudflare ingress/access policy metadata without secrets.
- Inspect input validation and authorization in Atlas module.
- Compare API responses for safe public diagnostics using controlled, authorized test targets.
- No production modifications during discovery.
