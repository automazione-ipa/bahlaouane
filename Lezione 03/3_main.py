from lib.pdf_reader import text_from_pdf
from lib.find_information import find_information

file_path = input("Enter the file path: ")
key = input("Enter the key to search for: ")

try:
    text = text_from_pdf(file_path)
    if text:
        information = find_information(text, key)
        
        if information:
            print(f"Information associated with '{key}': \n{information}")
        else:
            print(f"No information found for the key '{key}'.")
    else:
        print("No text was extracted from the PDF.")
        
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")