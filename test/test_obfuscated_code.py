import pytest
from malicious_pdf_generator import obfuscated_code
import const


@pytest.fixture
def sample_js_code():
    # Provide a sample JavaScript code
    return const.JS_CODE_TEST


def test_obfuscated_code_empty(sample_js_code):
    # Ensure that obfuscated code is not empty
    assert obfuscated_code(sample_js_code)


def test_obfuscated_code_different(sample_js_code):
    # Ensure that obfuscated code is different from original code
    assert obfuscated_code(sample_js_code) != sample_js_code
