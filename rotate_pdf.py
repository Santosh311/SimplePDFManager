from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate_pages(pdf_path, direction):
    pdf_read = PdfFileReader(pdf_path)
    pdf_write = PdfFileWriter()

    for page in range(pdf_read.getNumPages()):
        if direction.lower() == "clockwise":
            pdf_write.addPage(pdf_read.getPage(page).rotateClockwise(90))
        elif direction.lower() == "counter clockwise":
            pdf_write.addPage(pdf_read.getPage(page).rotateCounterClockwise(90))
        elif direction.lower() == "upside down":
            pdf_write.addPage(pdf_read.getPage(page).rotateClockwise(180))

    filename = pdf_path.split(".")[0]
    with open(f"{filename}_rotated.pdf","wb") as outfile:
        pdf_write.write(outfile)