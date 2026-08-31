import socket
import platform
import subprocess

def get_local_ip_info():
    print(f"\n[+] Local Machine Network Information")
    print("-" * 40)
    
    # Εύρεση Hostname και τοπικής IP
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = "Unable to resolve"
        
    print(f"Hostname      : {hostname}")
    print(f"Local IP      : {local_ip}")
    print(f"OS Platform   : {platform.system()} {platform.release()}")
    
    # Αν βρισκόμαστε σε Windows, μπορούμε να τραβήξουμε επιπλέον στοιχεία από το ipconfig
    if platform.system().lower() == "windows":
        print("\n[+] Active Network Interfaces (ipconfig summary):")
        print("-" * 40)
        try:
            output = subprocess.check_output("ipconfig", universal_newlines=True, encoding="cp737")
            for line in output.split("\n"):
                if "IPv4 Address" in line or "Default Gateway" in line or "Subnet Mask" in line:
                    print(line.strip())
        except Exception:
            pass
            
    print("-" * 40)

if __name__ == "__main__":
    get_local_ip_info()