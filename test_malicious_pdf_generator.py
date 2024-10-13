import os
from PyPDF2 import PdfReader
import pytest
from malicious_pdf_generator import embedded_javascript_into_pdf
from malicious_pdf_generator import obfuscated_code
from malicious_pdf_generator import check_open_action
from malicious_pdf_generator import const

@pytest.fixture
def sample_js_code():
    # Provide a sample JavaScript code
    return const.JS_CODE_TEST


@pytest.fixture
def input_pdf():
    return const.INPUT_PDF_DEFAULT


@pytest.fixture
def output_pdf():
    return const.OUTPUT_PDF_DEFAULT


def test_obfuscated_code_empty(sample_js_code):
    # Ensure that obfuscated code is not empty
    assert obfuscated_code(sample_js_code)


def test_obfuscated_code_different(sample_js_code):
    # Ensure that obfuscated code is different from original code
    assert obfuscated_code(sample_js_code) != sample_js_code


def test_check_open_action(output_pdf):
    # Check if the open action is present
    assert check_open_action(output_pdf)


def test_check_open_action_not(input_pdf):
    # Check if the open action is not present
    assert not check_open_action(input_pdf)


def test_embedded_javascript_into_pdf_output_file_exists(sample_js_code,
                                                         input_pdf,
                                                         output_pdf):
    # Execute the function
    embedded_javascript_into_pdf(sample_js_code, input_pdf, output_pdf)

    # Check if the output PDF file exists
    assert os.path.exists(output_pdf)


# work in progress
def test_embedded_javascript_into_pdf_input_file_exists(sample_js_code,
                                                         input_pdf,
                                                         output_pdf):
    # Execute the function
    embedded_javascript_into_pdf(sample_js_code, input_pdf, output_pdf)

    # Check if the input PDF file exists
    assert os.path.exists(input_pdf)

def test_embedded_javascript_into_pdf_output_open_action(sample_js_code,
                                                         input_pdf,
                                                         output_pdf):
    embedded_javascript_into_pdf(sample_js_code, input_pdf, output_pdf)

    assert check_open_action(output_pdf)

# work in progress. The following unit tests need further work
def test_embedded_javascript_into_pdf(sample_js_code, input_pdf, output_pdf):
    # Execute the function
    embedded_javascript_into_pdf(sample_js_code, input_pdf, output_pdf)

    # Check if the output PDF file exists
    assert os.path.exists(output_pdf)

    # Validate the content or properties of the output PDF file
    with open(output_pdf, 'rb') as file:
        reader = PdfReader(file)
        # Check if the number of pages is as expected
        assert len(reader.pages) > 0


def test_embedded_javascript_into_pdf_empty_js_code(input_pdf, output_pdf):
    # Execute the function with empty JavaScript code
    embedded_javascript_into_pdf("", input_pdf, output_pdf)
    # Check if the output PDF file exists
    assert os.path.exists(output_pdf)

def test_embedded_javascript_into_pdf_large_js_code(sample_js_code, input_pdf, output_pdf):
    # Create a large JavaScript code string
    large_js_code = "A" * 10000
    # Execute the function with large JavaScript code
    embedded_javascript_into_pdf(large_js_code, input_pdf, output_pdf)
    # Check if the output PDF file exists
    assert os.path.exists(output_pdf)

def test_embedded_javascript_into_pdf_IOError(sample_js_code, input_pdf,output_pdf):
    with pytest.raises(IOError, match="Error accessing file"):
        embedded_javascript_into_pdf(sample_js_code, "non_existent_input.pdf", output_pdf)

def test_embedded_javascript_into_pdf_Exception(monkeypatch, input_pdf, output_pdf):
    def mock_open(*args, **kwargs):
        raise Exception("Mocked exception")
    monkeypatch.setattr("builtins.open", mock_open)

    # Fix the regex to match the actual error message
    with pytest.raises(Exception, match="An error occurred : Mocked exception"):
        embedded_javascript_into_pdf("js_code", input_pdf, output_pdf)
