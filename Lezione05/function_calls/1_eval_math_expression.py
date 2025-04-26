import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")

# IMPOSTAZIONE DELL'ENDPOINT
url = "https://api.openai.com/v1/chat/completions"
# IMPOSTAZIONE DELL'HEADER con API KEY
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def calculate(expression: str):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Errore: {str(e)}"


def main():
    user_expression = input("Inserisci un'espressione matematica da calcolare (es. 2 + 2 * 3): ")

    function_schema = {
        "name": "calcola",
        "description": "Calcola un'espressione matematica.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Espressione da calcolare"
                }
            },
            "required": ["expression"]
        }
    }
    
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": f"valuta questa espressione {user_expression}"}
        ], "temperature": 0.7,
        "functions": [function_schema],
        "function_call": 'auto'
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

            if function_name == "calcola":
                result = calculate(function_args["expression"])
                print(f"Il risultato di {function_args['expression']} è: {result}")

        print("Risposta del modello:", response_message)

if __name__ == "__main__":
    main()
