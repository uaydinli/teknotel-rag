"""Offline regression tests. No network connection or systemd/GoBGP required."""
import pathlib
import subprocess
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
import service_smoke as s


class SmokeTests(unittest.TestCase):
    def test_established_peers(self):
        example = "Peer AS Up/Down State |#Received Accepted\n" \
                  "192.0.2.1 25145 2d Establ |100 100\n" \
                  "192.0.2.2 25145 2d Established |100 100\n"
        self.assertEqual((2, 0), s.parse_peer_states(example))

    def test_unhealthy_peer(self):
        self.assertEqual((1, 1), s.parse_peer_states(
            "192.0.2.1 25145 2d Establ |100 100\n192.0.2.2 25145 1m Active |0 0"))

    def test_non_peer_text_ignored(self):
        self.assertEqual((0, 0), s.parse_peer_states("BGP neighbor is Active\nHeader: Established"))

    @patch("service_smoke.subprocess.run")
    def test_rs_non_established_fails(self, run):
        run.return_value = subprocess.CompletedProcess([], 0, "192.0.2.1 25145 3h Active\n", "")
        result = s.check_gobgp(1, 1)
        self.assertEqual("FAIL", result.status)
        self.assertNotIn("192.0.2.1", result.detail)

    @patch("service_smoke.subprocess.run")
    def test_rs_unknown_format_warns(self, run):
        run.return_value = subprocess.CompletedProcess([], 0, "no neighbors", "")
        self.assertEqual("WARN", s.check_gobgp(1, 2).status)

    @patch("service_smoke.subprocess.run")
    def test_service_inactive(self, run):
        run.return_value = subprocess.CompletedProcess([], 3, "inactive\n", "")
        self.assertEqual("FAIL", s.check_service("gobgpd", 1).status)

    @patch("service_smoke.subprocess.run")
    def test_service_active(self, run):
        run.return_value = subprocess.CompletedProcess([], 0, "active\n", "")
        self.assertEqual("PASS", s.check_service("gobgpd", 1).status)

    @patch("service_smoke.socket.create_connection")
    def test_port_open(self, conn):
        ctx = MagicMock()
        conn.return_value = ctx
        self.assertEqual("PASS", s.check_tcp_port(5060, 1).status)
        conn.assert_called_once_with(("127.0.0.1", 5060), timeout=1)

    @patch("service_smoke.urllib.request.build_opener")
    def test_openapi_expected_route(self, build):
        response = MagicMock()
        response.getcode.return_value = 200
        response.read.return_value = b'{"paths":{"/api/test/start":{"post":{}}}}'
        build.return_value.open.return_value.__enter__.return_value = response
        self.assertEqual("PASS", s.check_json_api(8095, "/openapi.json", 1, "/api/test/start").status)
        self.assertEqual("FAIL", s.check_json_api(8095, "/openapi.json", 1, "/api/unknown").status)

    def test_redirects_disabled(self):
        handler = s.NoRedirect()
        self.assertIsNone(handler.redirect_request(None, None, 302, "Found", {}, "http://example.net"))

    @patch("service_smoke.urllib.request.build_opener")
    def test_invalid_json(self, build):
        response = MagicMock()
        response.getcode.return_value = 200
        response.read.return_value = b'<html>error</html>'
        build.return_value.open.return_value.__enter__.return_value = response
        self.assertEqual("FAIL", s.check_json_api(8095, "/api/health", 1).status)

    @patch("service_smoke.urllib.request.build_opener")
    def test_oversize_json(self, build):
        response = MagicMock()
        response.getcode.return_value = 200
        response.read.return_value = b"x" * (s.MAX_RESPONSE + 1)
        build.return_value.open.return_value.__enter__.return_value = response
        self.assertEqual("FAIL", s.check_json_api(8095, "/api/health", 1).status)

    def test_profiles(self):
        with patch.object(s, "check_service", return_value=s.Check("x", "PASS", "ok")), \
             patch.object(s, "check_tcp_port", return_value=s.Check("x", "PASS", "ok")), \
             patch.object(s, "check_json_api", return_value=s.Check("x", "PASS", "ok")), \
             patch.object(s, "check_gobgp", return_value=s.Check("x", "PASS", "ok")):
            self.assertEqual(6, len(s.run_profile("speedtest", 1, 2)))
            self.assertEqual(3, len(s.run_profile("lg", 1, 2)))
            self.assertEqual(2, len(s.run_profile("rs", 1, 2)))


if __name__ == "__main__":
    unittest.main()
