# Speedtest NIC and TCP checkpoint — 2026-10-23

Source: operator-supplied read-only ethtool, tc, ss and sysctl output from three Speedtest hosts.

## OBSERVED
- All three use vmxnet3 driver 1.7.0.0-k-NAPI, 8 combined channels.
- All use mq root with eight fq_codel child queues; observed qdisc dropped, overlimits and requeues counters zero.
- All use cubic TCP congestion control, fq_codel default qdisc, TCP SACK enabled, TCP timestamps enabled, TCP MTU probing disabled.
- TCP summary: speedtest-01 established=42 timewait=52 orphaned=7; speedtest-02 established=102 timewait=4959 orphaned=54; Ankara established=66 timewait=1 orphaned=0.
- Sample speedtest-01 socket lines include high rwnd_limited percentages. speedtest-02 samples include lost, sacked and retransmitted segments.

## LIMITS
- TCP socket and qdisc snapshots are workload-dependent; zero local qdisc drops do not rule out path loss.
- No evidence of an Ankara-specific guest NIC queue or congestion control configuration difference.
- No configuration changes or disruptive testing performed.

## NEXT
- Confirm hypervisor/uplink network policy and examine controlled client-server performance tests before attributing Ookla performance to a particular layer.
