import socket
import threading



HOST = '0.0.0.0'
PORT = 8080


clients = []


def handle_client(client_socket, client_address):
    print(f"[+] New client connected (ip address): {client_address}")
    clients.append(client_socket)

    try:
        while True:
            command = input("server > ")

            if command.lower() == "exit":
                break

            # Send command with a delimiter
            client_socket.send((command + "<END>").encode())

            # Receive response until the delimiter is found
            response = recv_until_end(client_socket, "<END>")
            print(f"[{client_address}] {response}")
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        print(f"[-] Disconnecting from client {client_address}")
        client_socket.close()
        clients.remove(client_socket)


def recv_until_end(sock, delimiter):
    data = b''
    while True:
        chunk = sock.recv(10000)
        if not chunk:
            break  # Connection closed
        data += chunk
        if delimiter.encode() in data:
            break
    return data.decode().replace(delimiter, "")  # Remove the delimiter



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[+] Start server {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
