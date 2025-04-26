import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")

url = "https://api.openai.com/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def read_file(file_name: str):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Errore: File non trovato."
    except Exception as e:
        return f"Errore durante la lettura del file: {str(e)}"

def main():
    file_name = input("Inserisci il nome del file da leggere: ")
    file_content = read_file(file_name)

    if file_content.startswith("Errore"):
        print(file_content)
        return

    print("\nContenuto del file caricato correttamente.\n")
    question = input("Ora scrivi una domanda basata sul contenuto del file: ")

    full_prompt = f"Ecco il contenuto di un file:\n{file_content}\n\nIn base a questo contenuto, rispondi alla domanda:\n{question}"

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.5,
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    if "error" in response_json:
        print("Errore nella risposta:", response_json["error"]["message"])
    else:
        response_message = response_json["choices"][0]["message"]
        print("\nRisposta del modello:", response_message["content"])

if __name__ == "__main__":
    main()
