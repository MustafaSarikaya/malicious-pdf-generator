import pypdf as pdf

output = pdf.PdfWriter()
ipdf = pdf.PdfReader(open('old.pdf', 'rb'))

for page in ipdf.pages:
    output.add_page(page)


with open('new.pdf', 'wb') as f:
    output.add_js("let a = 1; a = 10 + a; app.alert(a);")
    output.write(f)