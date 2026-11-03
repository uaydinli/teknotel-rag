#!/usr/bin/env python3
"""Read-only, localhost-first smoke checks for Teknotel Speedtest, LG and GoBGP RS.

Requires Python 3.10+ and only the standard library. Does not change live services,
install packages, run throughput benchmarks or publish sensitive configuration.
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import re
import socket
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass

MAX_RESPONSE = 256 * 1024
STATES = re.compile(r"\b(Established|Establ|Active|Idle|Connect|OpenSent|OpenConfirm)\b", re.I)


@dataclass(frozen=True)
class Check:
    name: str
    status: str
    detail: str


def check_service(unit: str, timeout: float) -> Check:
    try:
        p = subprocess.run(
            ["systemctl", "is-active", unit], check=False, capture_output=True,
            text=True, timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return Check(f"service:{unit}", "FAIL", type(exc).__name__)
    active = p.returncode == 0 and p.stdout.strip() == "active"
    return Check(f"service:{unit}", "PASS" if active else "FAIL",
                 "active" if active else "not active")


def check_tcp_port(port: int, timeout: float) -> Check:
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=timeout):
            pass
    except OSError as exc:
        return Check(f"tcp:127.0.0.1:{port}", "FAIL", type(exc).__name__)
    return Check(f"tcp:127.0.0.1:{port}", "PASS", "accepting local TCP connections")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def check_json_api(port: int, path: str, timeout: float, required_path: str | None = None) -> Check:
    # No redirects, no environment proxies, no external hosts, no query parameters.
    name = f"http:127.0.0.1:{port}{path}"
    url = f"http://127.0.0.1:{port}{path}"
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}),
                                         urllib.request.HTTPHandler(), NoRedirect())
    request = urllib.request.Request(url, headers={"Accept": "application/json"}, method="GET")
    try:
        with opener.open(request, timeout=timeout) as response:
            if response.getcode() != 200:
                return Check(name, "FAIL", f"HTTP {response.getcode()}")
            data = response.read(MAX_RESPONSE + 1)
    except urllib.error.HTTPError as exc:
        return Check(name, "FAIL", f"HTTP {exc.code}")
    except (urllib.error.URLError, OSError, TimeoutError) as exc:
        return Check(name, "FAIL", type(exc).__name__)
    if len(data) > MAX_RESPONSE:
        return Check(name, "FAIL", "response exceeds 256 KiB")
    try:
        body = json.loads(data)
    except (ValueError, UnicodeError):
        return Check(name, "FAIL", "invalid JSON")
    if not isinstance(body, dict):
        return Check(name, "FAIL", "JSON top level is not an object")
    if required_path is not None:
        routes = body.get("paths")
        if not isinstance(routes, dict) or required_path not in routes:
            return Check(name, "FAIL", f"OpenAPI path {required_path} missing")
        return Check(name, "PASS", f"OpenAPI includes {required_path}")
    return Check(name, "PASS", "HTTP 200; valid JSON object")


def parse_peer_states(output: str) -> tuple[int, int]:
    """Count recognizable summary-table states without exposing neighbor addresses."""
    established = 0
    other = 0
    for line in output.splitlines():
        # Accept only lines beginning with an IP address (IPv4 or IPv6).
        columns = line.split()
        if not columns:
            continue
        try:
            ipaddress.ip_address(columns[0])
        except ValueError:
            continue
        matches = STATES.findall(line)
        if not matches:
            continue
        state = matches[0].lower()
        if state in {"established", "establ"}:
            established += 1
        else:
            other += 1
    return established, other


def check_gobgp(timeout: float, expect_peers: int) -> Check:
    try:
        result = subprocess.run(
            ["gobgp", "neighbor"], capture_output=True, text=True,
            check=False, timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return Check("gobgp:neighbor", "FAIL", type(exc).__name__)
    if result.returncode != 0:
        return Check("gobgp:neighbor", "FAIL", f"exit code {result.returncode}")
    established, other = parse_peer_states(result.stdout)
    if other:
        return Check("gobgp:neighbor", "FAIL", f"{other} peers not Established; {established} Established")
    if established < expect_peers:
        return Check("gobgp:neighbor", "WARN",
                     f"parsed {established} Established; expected at least {expect_peers}; verify CLI format")
    return Check("gobgp:neighbor", "PASS", f"{established} Established peers")


def run_profile(profile: str, timeout: float, expect_peers: int) -> list[Check]:
    if profile == "speedtest":
        return [
            check_service("ooklaserver", timeout),
            check_service("teknotel-speedtest", timeout),
            check_tcp_port(5060, timeout),
            check_tcp_port(8080, timeout),
            check_json_api(8095, "/api/health", timeout),
            check_json_api(8095, "/openapi.json", timeout, "/api/test/start"),
        ]
    if profile == "lg":
        return [
            check_service("teknotel-lg", timeout),
            check_service("cloudflared", timeout),
            check_json_api(8080, "/openapi.json", timeout),
        ]
    if profile == "rs":
        return [
            check_service("gobgpd", timeout),
            check_gobgp(timeout, expect_peers),
        ]
    raise ValueError("unknown profile")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, choices=("speedtest", "lg", "rs"))
    parser.add_argument("--timeout", type=float, default=4.0)
    parser.add_argument("--expect-peers", type=int, default=2)
    parser.add_argument("--json", action="store_true", help="Machine-readable, redacted output")
    args = parser.parse_args()
    if not (0.1 <= args.timeout <= 30):
        parser.error("--timeout must be between 0.1 and 30 seconds")
    if not (0 <= args.expect_peers <= 128):
        parser.error("--expect-peers must be between 0 and 128")
    checks = run_profile(args.profile, args.timeout, args.expect_peers)
    if args.json:
        print(json.dumps({"profile": args.profile, "checks": [asdict(c) for c in checks]}, indent=2))
    else:
        for check in checks:
            print(f"{check.status:4} {check.name}: {check.detail}")
    return 1 if any(c.status == "FAIL" for c in checks) else 0


if __name__ == "__main__":
    sys.exit(main())
