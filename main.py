import PyPDF2 as pdf
import JsObfuscator as obfuscator
import const

try:

    with open('old.pdf', 'rb') as infile:
        ipdf = pdf.PdfReader(infile)

        output = pdf.PdfWriter()

        output.add_metadata(ipdf.metadata)

        for i, page in enumerate(ipdf.pages):

            if i == 0:
                page.rotate(90)
            output.add_page(page)

        obfuscated_java_script_code = obfuscator.obfuscated_code(const.JS_CODE)

        print(f"This is the obfuscated code : {obfuscated_java_script_code}")

        output.add_js(obfuscated_java_script_code)

        with open('new.pdf', 'wb') as outfile:
            output.write(outfile)

except IOError as e:
    print(f"Error accessing file: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
