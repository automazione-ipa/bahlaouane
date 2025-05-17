import requests
import json

def genera_ricetta_vegana(tipo_ricetta="primo"):
    url = "http://localhost:11434/api/generate"  # Assicurati che Ollama sia in esecuzione
    headers = {'Content-Type': 'application/json'}
    
    prompt = f"""
    Sei un esperto cuoco vegano. Crea una ricetta {tipo_ricetta} con:
    1. Nome della ricetta
    2. Ingredienti (formato markdown)
    3. Preparazione (passaggi numerati)
    4. Consiglio per una variante
    5. Tempo di preparazione e difficoltà
    """
    
    data = {
        "model": "veganchef",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(data),
            stream=False
        )
        
        if response.status_code == 200:
            ricetta = response.json()['response']
            print("--- RICETTA VEGANA ---")
            print(ricetta)
        else:
            print(f"Errore HTTP: {response.status_code}\n{response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Errore di connessione: {e}")
    except json.JSONDecodeError:
        print("Errore nel parsing della risposta JSON")

genera_ricetta_vegana("antipasto")