from lib.pdf_reader import text_from_pdf

DOC_PATH = "docs\\Lezione04_EstrarreTestoDaPDF.pdf"
DOC_PATH = "docs\\cv.pdf"

pdf_text = text_from_pdf(DOC_PATH)
if pdf_text:
    print(pdf_text)
else:
    print("No text was extracted from the PDF.")