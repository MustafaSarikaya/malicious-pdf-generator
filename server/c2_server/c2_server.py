import socket
import threading
import http.server
import socketserver


HOST = '0.0.0.0'
PORT = 8080


clients = []


def handle_client(client_socket, client_address):
    print(f"[+] New client connect (ip address): {client_address}")
    clients.append(client_socket)

    try:
        while True:

            command = input("server > ")


            if command.lower() == "exit":
                break


            client_socket.send(command.encode())


            response = client_socket.recv(1024).decode()
            print(f"[{client_address}] {response}")
    except Exception as e:
        print(f"[-] Error : {e}")
    finally:
        print(f"[-] Disconnect to the server {client_address}")
        client_socket.close()
        clients.remove(client_socket)


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
