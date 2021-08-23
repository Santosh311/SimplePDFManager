from PyPDF2 import PdfFileWriter, PdfFileReader

def encrypt_pdf(path, password):
    pdf_write = PdfFileWriter()
    pdf_read = PdfFileReader(path)

    for page in range(pdf_read.getNumPages()):
        pdf_write.addPage(pdf_read.getPage(page))

    pdf_write.encrypt(user_pwd=password, use_128bit=True)

    filename = path.split(".")[0]

    with open(f'{filename}_encrypted.pdf',"wb") as encrypted_pdf:
        pdf_write.write(encrypted_pdf)
    encrypted_pdf.close()