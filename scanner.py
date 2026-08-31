import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def check_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target_ip, port)) == 0:
            print(f"[+] Port {port} is open")
        s.close()
    except Exception:
        pass

def scan(target, ports):
    ip = socket.gethostbyname(target)
    print(f"[*] Scanning {ip} with threads...")
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for p in ports:
            executor.submit(check_port, ip, p)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <target>")
        sys.exit(1)
        
    ports_to_check = range(1, 1025)
    scan(sys.argv[1], ports_to_check)