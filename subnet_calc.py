import ipaddress
import sys

def calculate_subnet(network_input):
    try:
        # Δημιουργία αντικειμένου δικτύου με χρήση της βιβλιοθήκης ipaddress
        net = ipaddress.ip_network(network_input, strict=False)
        
        print(f"\n[+] Subnet Information for: {net}")
        print("-" * 40)
        print(f"Network Address : {net.network_address}")
        print(f"Broadcast IP    : {net.broadcast_address}")
        print(f"Netmask         : {net.netmask}")
        print(f"Wildcard Mask   : {net.hostmask}")
        print(f"Total Hosts     : {net.num_addresses}")
        print(f"Usable Hosts    : {max(net.num_addresses - 2, 0)}")
        print(f"IP Version      : IPv{net.version}")
        print("-" * 40)
        
    except ValueError as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <IP/CIDR>")
        print(f"Example: python {sys.argv[0]} 192.168.1.0/24")
        sys.exit(1)
        
    calculate_subnet(sys.argv[1])