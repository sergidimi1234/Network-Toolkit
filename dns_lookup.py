import socket
import sys

def dns_lookup(domain):
    print(f"\n[+] Performing DNS Lookup for: {domain}")
    print("-" * 40)
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address (A Record) : {ip}")
        
        hostname, aliases, ips = socket.gethostbyname_ex(domain)
        print(f"Canonical Name (CNAME): {hostname}")
        if aliases:
            print(f"Aliases               : {', '.join(aliases)}")
        if len(ips) > 1:
            print(f"All Associated IPs    : {', '.join(ips)}")
            
    except socket.gaierror as e:
        print(f"[-] Lookup failed: {e}")
    print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <domain_name>")
        print(f"Example: python {sys.argv[0]} google.com")
        sys.exit(1)
        
    dns_lookup(sys.argv[1])