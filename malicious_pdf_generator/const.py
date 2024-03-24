JS_CODE = """
var today = new Date();
var msg = 'PDF opened on: ' + today.toLocaleDateString() + ' ' + today.toLocaleTimeString();
app.alert(msg);
"""

JS_CODE_TEST = """
  app.alert("Hello PDF!");
"""

JS_OBFUSCATOR_LIBRARY = "javascript-obfuscator"
input_pdf = "old.pdf"
output_pdf = "new.pdf"
