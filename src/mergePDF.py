import pikepdf
from pikepdf import Pdf, Stream, Name

def merge_pdfs_with_js(source_pdf_path, js_code, output_pdf_path):
    # Load the existing PDF
    source_pdf = Pdf.open(source_pdf_path)

    # Create a new PDF to hold the JavaScript injection
    js_pdf = Pdf.new()
    
    # Create a single page in the new PDF (to hold the JS action)
    root = js_pdf.make_indirect({'Type': Name('/Catalog'),
                                 'Pages': js_pdf.make_indirect({'Type': Name('/Pages'),
                                                                'Kids': [js_pdf.make_indirect({'Type': Name('/Page'),
                                                                                               'MediaBox': [0, 0, 612, 792],
                                                                                              })],
                                                                'Count': 1,
                                                               })})
    js_pdf.root = root

    # Embed JavaScript in the new PDF
    js_stream = Stream(js_pdf, js_code.encode('utf-8'))
    js_action = js_pdf.make_indirect({'Type': Name('/Action'),
                                      'S': Name('/JavaScript'),
                                      'JS': js_stream})

    # Set the OpenAction of the new PDF to execute the JavaScript
    js_pdf.Root['OpenAction'] = js_action

    # Merge the existing PDF with the new PDF
    # Append pages from the source PDF to the new PDF
    js_pdf.pages.extend(source_pdf.pages)

    # Save the merged PDF with the JavaScript action
    js_pdf.save(output_pdf_path)

# JavaScript code you want to embed
js_code = """
// JavaScript code goes here
console.log('Hello, PDF!');
"""

# Path to the existing PDF you want to merge with
source_pdf_path = 'path_to_existing_pdf.pdf'

# Output file name for the merged PDF
output_pdf_path = 'merged_pdf_with_js.pdf'

# Merge the existing PDF with the new one containing the JavaScript injection
merge_pdfs_with_js(source_pdf_path, js_code, output_pdf_path)

print(f"Merged PDF created with embedded JavaScript: {output_pdf_path}")
