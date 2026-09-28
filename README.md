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

## Current Graylog investigation
The discovery scope is: stream rules, pipeline definitions, pipeline-to-stream bindings, pipeline rules, index sets, and index ranges.
The exact MongoDB command output is not present in the current repository context, so no unverified values are recorded.