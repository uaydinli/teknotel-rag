# Speedtest source review handoff — 2026-10-23

Status: inventory and network baseline established for three Speedtest VMs. Next step is application source audit, not repeated TCP sampling.

Review scope: Teknotel's Python/Uvicorn application, JavaScript/HTML/CSS frontend, Nginx server/proxy routes, effective Ookla configuration (redacted), and parity of deploy artifacts across hosts.

Method: read-only file lists, sizes and hashes first. Exclude credentials, secrets, certificates, databases, access logs, venv dependencies and backups from any transfer to a public repository. Review actual code offline before publishing sanitized material. Identify API surface and request/response behavior, implementation defects, security constraints and performance bottlenecks.

Network findings alone do not establish the root cause of Ankara's Ookla throughput result. No production changes authorized.
