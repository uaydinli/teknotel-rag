# Automatic GitHub Evidence Update Rule

Scope: current ChatGPT conversation for the Teknotel project.

## Rule
Whenever a discovery, debugging session, configuration inspection, packet analysis, test, or evidence-collection step produces a material result, update the GitHub repository as part of the same workflow. Do not wait for the user to repeat an instruction such as GitHub'a güncelle.

## Record
- Raw command/output evidence when available
- PCAP analysis findings
- Graylog stream/pipeline/index findings
- FortiDDoS/FortiGate/Juniper configuration findings
- Reproduction steps and test results
- Confirmed facts
- Hypotheses, explicitly marked as hypotheses
- Corrections to previous findings
- Relevant timestamps and source filenames

## Audit labels
OBSERVED = directly seen in evidence.
INFERRED = interpretation derived from observed evidence.
HYPOTHESIS = explanation that still requires verification.
VERIFIED = confirmed by a reproducible test or authoritative configuration.

Never turn an inference into an observed fact.

## Commit discipline
Use descriptive incremental commits such as evidence: record graylog stream discovery, debug: document pipeline routing finding, evidence: add pcap analysis, and fix: document verified configuration change.
Preserve earlier evidence when a later finding changes a conclusion; append the correction rather than silently rewriting history.