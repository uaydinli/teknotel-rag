# Speedtest / Looking Glass / Route Server — GitHub audit

Date: 2026-11-06
Target: `uaydinli/teknotel-rag` (PUBLIC)
Inspection: GitHub default branch tree, PR #1 metadata, GitHub Actions workflow and local offline tests.

## VERIFIED — Repository synchronization
- PR #1 (`feat/service-smoke-20261103`) was merged with a squash commit `4a58398eb437909ba2044dee2df4d9f2f57b3159`.
- The following four files are now on `main`:
  - `tools/service_smoke.py`
  - `tests/test_service_smoke.py`
  - `docs/SMOKE-TESTS.md`
  - `.github/workflows/service-smoke-unit.yml`
- GitHub Actions run 41704568390 for the PR head reported `completed / success`.
- Python compile and 13/13 offline unit tests passed in an isolated local runtime.
- None of these tests are measurements performed on production hosts.

## OBSERVED — Source artifact status
- A previously supplied ZIP contains an Ankara Native Speedtest backend `app.py` and frontend `index.html`.
- These are server snapshots, not an authenticated or reviewed release artifact. Only Ankara's source files are present in that ZIP.
- The GitHub repository does not currently contain complete deployable source trees for all three Speedtest sites, the Looking Glass API/frontend, or Route Server configuration.
- The repository is public. Do not copy potentially vulnerable production snapshots, unreviewed client-data handling, internal configuration or credentials directly into it.

## OPEN — Next source-level review
- Speedtest: reconcile three host versions, inspect Nginx limits and access policy, improve request bounding, IP/UA privacy and measurement correctness in a separate development branch.
- Looking Glass: obtain reviewed application source to validate authorization, target restrictions and MTR integration; maintain read-only diagnostic defaults.
- Route Server: verify source/config under controlled access and test peer state, policy assignment, export and FlowSpec separately. Do not commit unredacted BGP peer addresses or configuration to a public repository.

## Safety boundary
- No remote SSH, host modifications, BGP route writes, service restarts or real network throughput tests were performed by this GitHub synchronization.
- Recorded capabilities: smoke-test framework only; no production-ready claims for the three services.
