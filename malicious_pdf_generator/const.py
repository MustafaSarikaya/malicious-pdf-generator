# URL:
SERVER_URL: str = "https://www.google.ca"

# Payloads constants

JS_CODE = """
var today = new Date();
var msg = 'PDF opened on: ' + today.toLocaleDateString() + ' ' + today.toLocaleTimeString();
app.alert(msg);
"""

JS_CODE_TEST = """
  app.alert("Hello PDF!");
"""

PAYLOAD_LAUNCH_URL_OPEN_ACTION = f"""
    app.launchURL("{SERVER_URL}");
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
