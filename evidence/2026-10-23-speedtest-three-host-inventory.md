# Speedtest three-host discovery — 2026-10-23

Source: operator-supplied read-only terminal inventory from speedtest-01, speedtest-02 and Ankara.

## OBSERVED
- All three VMs run Ubuntu 24.04.4, VMware, 8 vCPU (Intel Xeon E5-2680 v3), 15 GiB RAM, ens192 10Gb/s Full Duplex, MTU 1500.
- Kernel versions: speedtest-01 and speedtest-02 6.8.0-146-generic; Ankara 6.8.0-139-generic.
- All three report running systemd services nginx, ooklaserver and teknotel-speedtest.
- Ookla listener ports: 5060 and 8080; Nginx 80 and 443; native Uvicorn API loopback port 8095 (four workers).
- All show /opt/ookla and /opt/ooklaserver directories; active process path from ps is /opt/ookla/OoklaServer.
- NIC RX error 0 and TX error 0 on all three; cumulative RX dropped counters 627 (01), 400 (02), 74 (Ankara). No TX drops shown.
- Swap usage 0 at capture time on all hosts. System indicates restart required on all three.
- Host network addresses, interfaces and credentials are not stored in this public evidence record.

## LIMITATIONS
- NIC negotiated 10Gb/s is not a verified end-to-end throughput benchmark.
- Counters are cumulative, not a packet-drop rate or time series.
- No CPU stress, link saturation, hypervisor shaping, upstream routing or Ookla workload measurements were performed.
- Mapping from commercial server ID to these hostnames requires explicit confirmation; no claims of which speedtest-XX represents which geographic site.

## NEXT READ-ONLY INSPECTION
- Inspect actual Ookla version and redacted active config, service flags, Nginx upstream, system network counters and hardware offload configuration.
- Confirm server ID / geographic mappings from authoritative service records.
- Do not run active throughput tests or change production services during initial discovery.
