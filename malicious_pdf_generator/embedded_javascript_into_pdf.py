import pypdf as pdf


def embedded_javascript_into_pdf(js_code, input_pdf, output_pdf):
    """
    Embeds JavaScript code into a PDF file.

    Parameters:
        js_code (str): The JavaScript code to embed.
        input_pdf (str): The path to the input PDF file.
        output_pdf (str): The path to save the output PDF file.

    Raises:
        IOError: If there is an error accessing the input or output PDF files.
        Exception: If an unexpected error occurs during the process.
    """
    try:
        with open(input_pdf, 'rb') as infile:
            ipdf = pdf.PdfReader(infile)

            output = pdf.PdfWriter()

            output.add_metadata(ipdf.metadata)

            for i, page in enumerate(ipdf.pages):
                output.add_page(page)

            output.add_js(js_code)

            with open(output_pdf, 'wb') as outfile:
                output.write(outfile)

    except IOError as e:
        print(f"Error accessing file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

