# Auto Download Server

This is a Node.js server designed to automatically download files. The server is containerized using Docker for easy installation and deployment.

## Prerequisites

- Docker
- Node.js v22
- Python v12

## Installation

1. Build the Docker image:
    ```sh
    docker build -t auto-download-server .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 3000:3000 auto-download-server
    ```

3. The server should now be running. You can access it at `http://localhost:3000`.

## Usage

To use the auto-download server, simply access `http://localhost:3000` in your browser.


## c2_client.py

The `c2_client.py` script is used to interact with the Command and Control (C2) server. It allows you to send commands and receive responses from the server. Ensure that the C2 server is running and properly configured before using this script.

## Disclaimer

This project is intended for research purposes only. Do not use it to attack or harm others.
