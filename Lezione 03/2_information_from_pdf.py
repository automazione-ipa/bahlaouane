from lib.pdf_reader import text_from_pdf
from lib.find_information import find_information

DOC_PATH = "docs\\cv.pdf"

pdf_text = text_from_pdf(DOC_PATH)
if pdf_text:
    key = "vendite"
    information = find_information(pdf_text, key)
    
    if information:
        print(f"Information associated with '{key}': \n{information}")
    else:
        print(f"No information found for the key '{key}'.")        
else:
    print("No text was extracted from the PDF.")
   
