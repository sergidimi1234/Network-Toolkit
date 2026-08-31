# Network-Toolkit

A lightweight and fast network utility toolkit written in Python. Designed for quick reconnaissance, port scanning, network diagnostics, and messaging.

## Tools Included

### 1. Multi-threaded Port Scanner (`scanner.py`)
A fast TCP port scanner that utilizes multithreading (`ThreadPoolExecutor`) to scan target ports efficiently and identifies running services.
* **Features:** Fast multi-threaded scanning, target resolution (Domain name to IP), automatic service detection.
* **Usage:** 
```bash
python scanner.py <target_ip_or_domain>
python subnet_calc.py <IP/CIDR>
python ip_monitor.py
python dns_lookup.py <domain_name>
python chat_server.py
python chat_client.py <server_ip>
