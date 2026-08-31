import socket
import sys

def start_client(host='127.0.0.1', port=9999):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        print(f"[+] Connected to server at {host}:{port}")
        
        while True:
            message = input("Client > ")
            client.send(message.encode('utf-8'))
            if message.lower() == 'exit':
                break
                
            response = client.recv(1024).decode('utf-8')
            if not response or response.lower() == 'exit':
                print("[-] Server disconnected.")
                break
            print(f"Server > {response}")
            
    except Exception as e:
        print(f"[-] Connection failed: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    target_ip = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    start_client(target_ip)