import PyPDF2 as pdf

try:

    with open('old.pdf', 'rb') as infile:
        ipdf = pdf.PdfReader(infile)

        output = pdf.PdfWriter()

        output.add_metadata(ipdf.metadata)

        for i, page in enumerate(ipdf.pages):

            if i == 0:
                page.rotate(90)
            output.add_page(page)

        js_code = """
        var today = new Date();
        var msg = 'PDF opened on: ' + today.toLocaleDateString() + ' ' + today.toLocaleTimeString();
        app.alert(msg);
        """

        output.add_js(js_code)

        with open('new.pdf', 'wb') as outfile:
            output.write(outfile)

except IOError as e:
    print(f"Error accessing file: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
