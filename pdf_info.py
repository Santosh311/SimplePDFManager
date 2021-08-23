from PyPDF2 import PdfFileReader

def getPDFInfo(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf = PdfFileReader(pdf_file)
        info = pdf.getDocumentInfo()
        no_of_pages = pdf.getNumPages()

    str = f"""
    Information about {pdf_path}:-
    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Title: {info.title}
    Number of Pages: {no_of_pages}
    """
    return str