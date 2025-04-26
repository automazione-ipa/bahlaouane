import os
import json
import requests
import wikipedia
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")

url = "https://api.openai.com/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def wikipedia_summary(query: str):
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except wikipedia.exceptions.PageError:
        return "Errore: Nessuna pagina trovata per questa query."
    except Exception as e:
        return f"Errore generico: {str(e)}"

function_schema = {
    "name": "wikipedia_summary",
    "description": "Cerca un argomento su Wikipedia e restituisce un breve riassunto.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "L'argomento di cui cercare il riassunto su Wikipedia"
            }
        },
        "required": ["query"]
    }
}

def main():
    user_question = input("Fai una domanda di cultura generale: ")

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": user_question}
        ],
        "temperature": 0.7,
        "functions": [function_schema],
        "function_call": "auto"
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    print(f"Response status code: {response.status_code}\n")

    if "error" in response_json:
        print("Errore nella risposta:", response_json["error"]["message"])
    else:
        response_message = response_json["choices"][0]["message"]
        
        if response_message.get("function_call"):
            function_name = response_message["function_call"]["name"]
            function_args = json.loads(response_message["function_call"]["arguments"])

            print(f"Funzione suggerita: {function_name}")
            print(f"Argomenti: {function_args}")

            if function_name == "wikipedia_summary":
                result = wikipedia_summary(function_args["query"])
                print(f"\nRisposta: {result}")
        else:
            print("Risposta del modello:", response_message["content"])

if __name__ == "__main__":
    main()
