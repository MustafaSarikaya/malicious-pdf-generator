#!/usr/bin/env python3

import os
import sys
import paramiko
from scp import SCPClient
from pathlib import Path

def create_ssh_client(host, port, username, key_filepath):
    """Create and return an SSH client connected to the specified host."""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=host,
            port=port,
            username=username,
            key_filename=key_filepath
        )
        return ssh
    except Exception as e:
        print(f"[ERROR] Failed to establish SSH connection: {e}")
        sys.exit(1)

def transfer_file(ssh, local_path, remote_path):
    """Transfer a file to the remote host using SCP."""
    try:
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(local_path, remote_path)
        print(f"[INFO] Successfully transferred {local_path} to {remote_path}")
    except Exception as e:
        print(f"[ERROR] Failed to transfer file: {e}")
        sys.exit(1)

def execute_powershell_script(ssh, script_path, pdf_path):
    """Execute a PowerShell script on the remote Windows VM via SSH."""
    try:
        # Build the command
        powershell_command = f'powershell.exe -ExecutionPolicy Bypass -File {script_path} -PdfPath {pdf_path}'

        # Execute the command on the remote VM
        stdin, stdout, stderr = ssh.exec_command(powershell_command)

        # Read the output and errors
        output = stdout.read().decode()
        errors = stderr.read().decode()

        if output:
            print("[INFO] PowerShell script output:")
            print(output)
        if errors:
            print("[ERROR] PowerShell script errors:")
            print(errors)
    except Exception as e:
        print(f"[ERROR] Failed to execute PowerShell script: {e}")
        sys.exit(1)

# Ensure the script can be imported without running the main function
if __name__ == "__main__":
    def parse_arguments():
        """Parse command-line arguments."""
        parser = argparse.ArgumentParser(description="Deploy PDF to VM via SSH.")
        parser.add_argument(
            "pdf_path",
            type=str,
            help="Path to the PDF file to be deployed."
        )
        parser.add_argument(
            "--host",
            type=str,
            default="localhost",
            help="IP address or hostname of the VM."
        )
        parser.add_argument(
            "--port",
            type=int,
            default=22,
            help="SSH port of the VM (default: 22)."
        )
        parser.add_argument(
            "--username",
            type=str,
            required=True,
            help="Username for SSH connection."
        )
        parser.add_argument(
            "--key",
            type=str,
            default=str(Path.home() / ".ssh" / "id_rsa"),
            help="Path to the SSH private key (default: ~/.ssh/id_rsa)."
        )
        parser.add_argument(
            "--remote-dir",
            type=str,
            default="/path/to/remote/directory/",
            help="Destination directory on the VM."
        )
        return parser.parse_args()

    def main():
        args = parse_arguments()

        # Validate PDF path
        local_pdf = Path(args.pdf_path)
        if not local_pdf.is_file() or local_pdf.suffix.lower() != ".pdf":
            print(f"[ERROR] The file {args.pdf_path} does not exist or is not a PDF.")
            sys.exit(1)

        # Validate SSH key path
        key_path = Path(args.key)
        if not key_path.is_file():
            print(f"[ERROR] The SSH key file {args.key} does not exist.")
            sys.exit(1)

        # Establish SSH connection
        ssh_client = create_ssh_client(
            host=args.host,
            port=args.port,
            username=args.username,
            key_filepath=str(key_path)
        )

        # Define remote file path
        remote_file_path = os.path.join(args.remote_dir, local_pdf.name)

        # Transfer the PDF
        transfer_file(ssh_client, str(local_pdf), remote_file_path)

        # Execute PowerShell script on the VM
        script_path = 'C:\\Users\\vboxuser\\scripts\\Open-Pdf-interactive.ps1'  # Update as needed
        execute_powershell_script(ssh_client, script_path, remote_file_path)

        # Close SSH connection
        ssh_client.close()

    main()
