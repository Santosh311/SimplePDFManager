from PyPDF2 import PdfFileWriter, PdfFileReader

def extract_page(path, page_no):
    pdf_read = PdfFileReader(path)
    pdf_write = PdfFileWriter()

    pdf_write.addPage(pdf_read.getPage(page_no-1))
    filename = path.split(".")[0]
    with open(f"{filename} page{page_no}.pdf", "wb") as output_stream:
        pdf_write.write(output_stream)