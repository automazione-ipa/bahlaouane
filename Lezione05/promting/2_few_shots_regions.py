import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")
SHOT =  {
    "regione": "Piemonte",
    "capoluogo": "Torino",
    "abitanti": 4307000,
    "province": [
        "Alessandria",
        "Asti",
        "Biella",
        "Cuneo",
        "Novara",
        "Torino",
        "Verbano-Cusio-Ossola",
        "Vercelli"
    ],
    "natalita": 6.8,
    "mete_turistiche": [
        "Mole Antonelliana (Torino)",
        "Palazzi Reali di Torino",
        "Langhe e Roero (patrimonio UNESCO)",
        "Lago Maggiore",
        "Monviso",
        "Sacra di San Michele",
        "Asti e il suo Palio"
    ],
    "specialita_culinarie": [
        "Bagna càuda",
        "Tajarin",
        "Agnolotti del Plin",
        "Vitello Tonnato",
        "Bollito misto alla piemontese",
        "Bonet",
        "Grissini",
        "Barolo e Barbaresco (vini)"
    ]
}

# IMPOSTAZIONE DELL'ENDPOINT
url = "https://api.openai.com/v1/chat/completions"
# IMPOSTAZIONE DELL'HEADER con API KEY
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

region = input("Per quale regione vuoi recuperare informazioni? ")

prompt = f"""genera un json recuperando informazioni per questa regione: {region}
        Il json deve contenere nome della regione, capoluogo, numero abitanti, lista province, natalità, mete turistiche, specialità culinarie.
        Di seguito un json di esempio per la regione {SHOT}""" 

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": prompt}
    ], "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

print(f"Response status code: {response.status_code}")
print(response.json()["choices"][0]["message"]["content"])
