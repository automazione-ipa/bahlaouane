import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")

# IMPOSTAZIONE DELL'ENDPOINT
url = "https://api.openai.com/v1/chat/completions"
# IMPOSTAZIONE DELL'HEADER con API KEY
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

countries = []

while len(countries) == 0:
    user_input = input("Inserisci 3 paesi separati da virgola (es. Italia, Francia, Spagna): ")
    countries = [country.strip() for country in user_input.split(",") if country.strip()]  # Skip empty

prompt = f"indicami la capitale di: {countries}"

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": prompt}
    ], "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

print(f"Response status code: {response.status_code}\n")
print(response.json()["choices"][0]["message"]["content"])