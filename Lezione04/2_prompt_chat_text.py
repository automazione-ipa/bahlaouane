import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")
DOC_PATH = "docs\\es2_text.txt"

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


text = read_file(DOC_PATH)

if(text):        
    # IMPOSTAZIONE DELL'ENDPOINT
    url = "https://api.openai.com/v1/chat/completions"
    # IMPOSTAZIONE DELL'HEADER con API KEY
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    question = input("Cosa vuoi chiedere a ChatGPT? ")

    prompt = f"estrai la risposta alla mia domanda: {question} da questo testo: {text}"
    print(API_KEY)
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