# Auto Download Server and C2 Server

This repository contains two interconnected projects designed for research purposes: a **Command and Control (C2) Server** and an **Auto Download Server**. These tools work together to simulate a controlled environment for testing client-server interactions. The Auto Download Server facilitates the download of the agent, while the C2 Server controls the machine running the agent (`c2_client.py`).

---

## System Overview

### Workflow
1. **Auto Download Server**: Hosts and serves the agent file (`c2_client.py`) for download.
2. **C2 Client**: Once downloaded, the agent (`c2_client.py`) executes on the target machine.
3. **C2 Server**: Manages and controls the machines running the `c2_client.py` script, allowing commands to be sent and responses to be received.

### Example Use Case
- A user downloads the `c2_client.py` script via the **Auto Download Server**.
- The downloaded script connects to the **C2 Server** and becomes an active client.
- The **C2 Server** can now issue commands to the client and monitor its responses.

---

## Auto Download Server

### Description
The Auto Download Server is a Node.js-based service containerized with Docker, providing an easy-to-deploy file download server.

### Prerequisites
- Docker
- Node.js v22
- Python v12

### Installation
1. Build the Docker image:
    ```sh
    docker build -t auto-download-server .
    ```
2. Run the Docker container:
    ```sh
    docker run -p 3000:3000 auto-download-server
    ```
3. The server should now be running. You can access it at `http://localhost:3000`.

### Usage
Access the **Auto Download Server** at `http://localhost:3000` to download the agent (`c2_client.py`).

---

## C2 Server

### Description
The C2 Server is designed to manage machines running the `c2_client.py` script. It provides full command and control (C2) functionality, including sending commands, receiving responses, and logging client activities.

### Features
- Manage multiple clients
- Send commands to clients
- Receive responses from clients
- Log client activities

### Installation
1. Navigate to the C2 Server directory:
    ```sh
    cd /path/to/malicious-pdf-generator/server/c2_server
    ```

### Usage
1. Start the C2 Server:
    ```sh
    python server.py
    ```
2. Connect clients to the server by executing the `c2_client.py` script on the target machines.

---

## c2_client.py

### Description
The `c2_client.py` script is the agent that establishes a connection to the **C2 Server**. It allows the server to send commands and receive responses.

### Usage
1. Download the `c2_client.py` script from the **Auto Download Server**.
2. Execute the script on the target machine:
    ```sh
    python c2_client.py
    ```
3. The script will connect to the **C2 Server** for management and control.

---

## Disclaimer

These projects are strictly for research and educational purposes. Unauthorized or malicious use of this software is strictly prohibited. The authors are not responsible for any misuse of this software.
