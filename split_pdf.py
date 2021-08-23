from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(path, num_page, name_of_pdfs):
    pdf_read = PdfFileReader(path)
    pdf_write1 = PdfFileWriter()

    for page in range(num_page):
        pdf_write1.addPage(pdf_read.getPage(page))

    output1 = f'{name_of_pdfs}_0.pdf'
    with open(output1,"wb") as pdf_1:
        pdf_write1.write(pdf_1)

    pdf_write2 = PdfFileWriter()

    for page in range(num_page, pdf_read.getNumPages()):
        pdf_write2.addPage(pdf_read.getPage(page))

    output2 = f'{name_of_pdfs}_1.pdf'
    with open(output2, "wb") as pdf_2:
        pdf_write2.write(pdf_2)
    pdf_2.close()