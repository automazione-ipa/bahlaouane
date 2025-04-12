import requests
from lib.pdf_reader import text_from_pdf
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")
DOC_PATH = "docs\\cv.pdf"

pdf_text = text_from_pdf(DOC_PATH)
if pdf_text:
    # IMPOSTAZIONE DELL'ENDPOINT
    url = "https://api.openai.com/v1/chat/completions"
    # IMPOSTAZIONE DELL'HEADER con API KEY
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    question = input("Cosa vuoi chiedere a ChatGPT? ")

    prompt = f"estrai la risposta alla mia domanda: {question} da questo testo: {pdf_text}"

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ], "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    print(f"Response status code: {response.status_code}")
    print(response.json()["choices"][0]["message"]["content"])

else:
    print("No text was extracted from the PDF.")
 
    
    