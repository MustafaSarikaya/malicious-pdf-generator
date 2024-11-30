from malicious_pdf_generator import obfuscated_code, embedded_javascript_into_pdf, create_ssh_client, transfer_file, execute_powershell_script, fetch_alerts, analyze_alerts, const

import argparse
import pyfiglet
import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

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

    :return: str: The selected payload to embed in the PDF file.
    """
    payload = None  # Initialize the payload as None

    while payload is None:  # Loop until a valid payload is chosen
        print("Choose the payload to embed into the PDF file:")
        print("1. Download file (URL action)")
        print("2. Alert message")
        print("3. Collect information using Grabify (URL action)")

        # Additional payload options (currently not implemented):
        # print("4. Adobe Reader Calculate Crash")
        # print("5. Adobe Reader Font Exploit Shellcode")
        # print("6. Dropper")

        try:
            # Prompt the user for input and convert it to an integer
            choice = int(input("Enter the payload number: "))

            # Map user input to the corresponding payload
            if choice == 1:
                payload = const.PAYLOAD_DOWNLOAD_FILE
            elif choice == 2:
                payload = const.JS_CODE
            elif choice == 3:
                payload = const.PAYLOAD_COLLECT_INFORMATION_USING_GRABIFY
            # Future implementation placeholders for other payloads:
            # elif choice == 4:
            #     payload = const.PAYLOAD_MOCK_ADOBE_CRASH
            # elif choice == 5:
            #     payload = const.PAYLOAD_MOCK_SHELLCODE_ADOBE_EXPLOIT
            # elif choice == 6:
            #     payload = const.PAYLOAD_DROPPER
            else:
                # Handle invalid input outside the defined range
                print("Invalid choice. Please try again.")
        except ValueError:
            # Handle non-integer input errors
            print("Invalid input. Please enter a number.")

    return payload  # Return the selected payload


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
    # SSH Connection Details
    host = os.getenv('SSH_HOST', 'localhost')
    port = int(os.getenv('SSH_PORT', 22))
    username = os.getenv('SSH_USERNAME')
    key_filepath = os.path.expanduser(os.getenv('SSH_KEY_PATH', '~/.ssh/id_rsa'))
    
    # Remote VM Directories
    remote_dir = os.getenv('REMOTE_DIR')
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
    transfer_file(ssh_client, local_pdf_path, remote_dir)

    # Execute the PowerShell script on the VM
    remote_script_path = os.getenv('REMOTE_SCRIPT_PATH')
    execute_powershell_script(ssh_client, remote_script_path, remote_pdf_path)

    # Close SSH connection
    ssh_client.close()

    # Wait for Elastic Stack to process the alert
    import time
    # Other Configurations
    wait_time = int(os.getenv('WAIT_TIME', 30))

    print("[INFO] Waiting for Elastic Stack to process alerts...")
    time.sleep(wait_time)  # Wait 30 seconds; adjust as needed

    # Fetch alerts from Elastic Stack
    # Elasticsearch Host and Port
    elastic_host = os.getenv('ELASTIC_HOST', 'localhost')
    elastic_port = int(os.getenv('ELASTIC_PORT', 9200))
    
    # Elastic Stack Credentials
    elastic_username = os.getenv('ELASTIC_USERNAME')
    elastic_password = os.getenv('ELASTIC_PASSWORD')
    
    pdf_name = os.path.basename(local_pdf_path)
    alerts = fetch_alerts(elastic_host, elastic_port, elastic_username, elastic_password, pdf_name)

    # Analyze alerts and output results
    log_file_path = os.getenv('LOG_FILE_PATH', 'alert_results.log')
    analyze_alerts(alerts, pdf_name, log_file_path)

if __name__ == "__main__":
    main()
