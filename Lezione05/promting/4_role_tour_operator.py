import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")

url = "https://api.openai.com/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

messages = []

destination = input("Inserisci la destinazione del tuo viaggio: ")

initial_prompt = f"""Agisci come un operatore turistico esperto. Il tuo compito è aiutarmi a pianificare un viaggio perfetto.
Fai domande per capire le mie preferenze su destinazione, periodo, budget, interessi (es. cultura, natura, relax),
tipo di alloggio e mezzi di trasporto preferiti. Poi suggerisci un itinerario dettagliato, attività da fare, dove mangiare
e consigli utili. Sii cordiale e professionale. Voglio partire per {destination}."""

messages.append({"role": "user", "content": initial_prompt})

def get_response(messages):
    data = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

reply = get_response(messages)
print(f"\nAssistente:\n{reply}")
messages.append({"role": "assistant", "content": reply})

while True:
    user_input = input("\nTu: ")
    if user_input.lower() in ["esci", "exit"]:
        print("Conversazione terminata. Buon viaggio!")
        break
    messages.append({"role": "user", "content": user_input})
    reply = get_response(messages)
    print(f"\nAssistente:\n{reply}")
    messages.append({"role": "assistant", "content": reply})
