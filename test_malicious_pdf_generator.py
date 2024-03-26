import os
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


def test_embedded_javascript_into_pdf_output_open_action(sample_js_code,
                                                         input_pdf,
                                                         output_pdf):
    embedded_javascript_into_pdf(sample_js_code, input_pdf, output_pdf)

    assert check_open_action(output_pdf)
