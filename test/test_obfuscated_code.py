import pytest
from malicious_pdf_generator import obfuscated_code
import const


def test_obfuscated_code():
    js_code = const.JS_CODE_TEST

    obfuscated_js_code = obfuscated_code(js_code)

    # Ensure that obfuscated code is not empty
    assert obfuscated_js_code

    # Ensure that obfuscated code is different from original code
    assert obfuscated_js_code != js_code
