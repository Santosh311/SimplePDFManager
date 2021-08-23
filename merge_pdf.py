from PyPDF2 import PdfFileWriter, PdfFileReader
import warnings

def merge_pdfs(paths, output):
    pdf_write = PdfFileWriter()

    for pdf in paths:
        pdf_read = PdfFileReader(pdf)
        for i in range(pdf_read.getNumPages()):
            pdf_write.addPage(pdf_read.getPage(i))

    with open(output,"wb") as merged:
        pdf_write.write(merged)
    merged.close()