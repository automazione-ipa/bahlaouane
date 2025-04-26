import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")

# IMPOSTAZIONE DELL'ENDPOINT
url = "https://api.openai.com/v1/chat/completions"
# IMPOSTAZIONE DELL'HEADER con API KEY
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

prompt = "usa il CoT per generare i primi 10 numeri di fibonacci"

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": prompt}
    ], "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

print(f"Response status code: {response.status_code}\n")
print(response.json()["choices"][0]["message"]["content"])
