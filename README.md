[README.md](https://github.com/user-attachments/files/31660629/README.md)
\# Network-Toolkit 
A lightweight and fast network utility toolkit written in Python. Designed for quick reconnaissance, port scanning, and network diagnostics.
\## Tools Included
\### 1. Multi-threaded Port Scanner (`scanner.py`)
A fast TCP port scanner that utilizes multithreading (`ThreadPoolExecutor`) to scan target ports efficiently and identifies running services.
\#### Features:\- Fast multi-threaded scanning\- Target resolution (Domain name to IP)\- Automatic service detection (`http`, `microsoft-ds`, etc.)
\#### Usage:```bash
python scanner.py <target\_ip\_or\_domain>
