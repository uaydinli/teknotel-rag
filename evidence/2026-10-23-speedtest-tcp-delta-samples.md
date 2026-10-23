# Speedtest TCP rate samples — 2026-10-23

Operator-supplied ten-second read-only `nstat -az` interval samples (rates per second).

| Server | TcpRetransSegs/s | TcpExtTCPTimeouts/s | TcpExtTCPSynRetrans/s |
|---|---|---|---|
| speedtest-01 #1 | 27.08 | 1.40 | 0.30 |
| speedtest-01 #2 | 284.77 | 16.49 | 0.40 |
| speedtest-02 #1 | 4643.17 | 3.80 | 2.20 |
| speedtest-02 #2 | 2858.12 | 6.20 | 2.30 |
| Ankara #1 | 0 | 0 | 0 |
| Ankara #2 | 0 | 0 | 0 |
| Ankara #3 | 166.71 | 1.60 | 0 |
| Ankara #4 | 4.50 | 0 | 0 |
| Ankara #5 | 0.20 | 0 | 0 |
| Ankara #6 | 0 | 0 | 0 |

All observed TcpExtTCPBacklogDrop deltas were zero.

These are segment counts per second, not packet loss percentage. Traffic volumes and active test load were not measured. High absolute values on speedtest-02 warrant network/path inspection but do not establish fault causality. Next: sample TcpOutSegs, retransmissions, NIC RX/TX bytes over same period, and inspect socket-level TCP metrics.
