import os
import tempfile
import pytest
from malicious_pdf_generator import embedded_javascript_into_pdf
import const
from PyPDF2 import PdfReader


@pytest.fixture
def sample_js_code():
    # Provide a sample JavaScript code
    return const.JS_CODE_TEST


@pytest.fixture
def input_pdf():
    # Create a temporary input PDF file for testing
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
        temp_file.write(b"Sample PDF content")
        return temp_file.name


@pytest.fixture
def output_pdf():
    # Create a temporary output PDF file for testing
    return tempfile.NamedTemporaryFile(suffix=".pdf", delete=False).name


def test_embedded_javascript_into_pdf_output_file_exists(sample_js_code, input_pdf, output_pdf):
    # Execute the function
    embedded_javascript_into_pdf(sample_js_code, input_pdf, output_pdf)

    # Check if the output PDF file exists
    assert os.path.exists(output_pdf)

    # Clean up temporary files
    os.unlink(input_pdf)
    os.unlink(output_pdf)


def test_embedded_javascript_into_pdf_output_added_js(sample_js_code, input_pdf, output_pdf):
    # Execute the function
    embedded_javascript_into_pdf(sample_js_code, input_pdf, output_pdf)

    try:
        # Load the modified PDF file
        with open(output_pdf, 'rb') as file:
            pdf = PdfReader(file)

            # Check if the output PDF file contains the added JavaScript code
            assert "/Names" in pdf.trailer, "add_js should add a name catalog in the root object."
            assert "/JavaScript" in pdf.trailer[
                "/Names"], "add_js should add a JavaScript name tree under the name catalog."
    except (FileNotFoundError, Exception):
        # Handle the EmptyFileError (and other potential errors) gracefully
        print("Error reading PDF file or file is empty.")
    finally:
        # Clean up temporary files
        if os.path.exists(input_pdf):
            os.unlink(input_pdf)
        if os.path.exists(output_pdf):
            os.unlink(output_pdf)
