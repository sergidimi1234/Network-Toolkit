import socket
import sys

def start_server(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"[*] Server listening on {host}:{port}...")
    
    client, addr = server.accept()
    print(f"[+] Connection accepted from {addr[0]}:{addr[1]}")
    
    while True:
        message = client.recv(1024).decode('utf-8')
        if not message or message.lower() == 'exit':
            print("[-] Client disconnected.")
            break
        print(f"Client > {message}")
        
        response = input("Server > ")
        client.send(response.encode('utf-8'))
        if response.lower() == 'exit':
            break
            
    client.close()
    server.close()

if __name__ == "__main__":
    start_server()