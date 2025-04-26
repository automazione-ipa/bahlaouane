import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("ALFASOFT_IPA_OPENAI_KEY")


def zero_shot_prompt(question):
    return question

def few_shot_prompt(question):
    examples = ask_model(zero_shot_prompt, f"fornisci esempi per questa domanda: {question}")
    print(f"\nho identificato questi esempi: {role.json()["choices"][0]["message"]["content"]}")

    return f"Rispondi a questa domanda: {question}, questi esempi potrebbero aiutarti: {examples}"

def cot_prompt(question):
    return f"Rispondi passo per passo alla seguente domanda:\n{question}"

def react_prompt(question):
    return f"Pensa in modo logico e agisci per rispondere alla domanda seguente:\n{question}"

def tree_of_thought_prompt(question):
    return f"Esplora possibili soluzioni alla domanda come se stessi seguendo rami di un albero decisionale:\n{question}"

def generated_knowledge_prompt(question):
    return f"Prima genera conoscenze utili sull'argomento, poi rispondi alla domanda:\n{question}"

def iterative_refinement_prompt(question):
    return f"Fornisci una prima risposta, poi raffinala passo dopo passo:\n{question}"

def self_consistency_prompt(question):
    return f"Genera più risposte alla seguente domanda, poi seleziona quella più coerente:\n{question}"

def role_prompting_prompt(question):
    role = ask_model(zero_shot_prompt, f"secondo te quale ruolo esperto dovresti impersonificare per rispondere a questa domanda? {question}?. Limitati a dirmi il ruolo")
    print(f"\nho identificato questo ruolo: {role.json()["choices"][0]["message"]["content"]}")
    return f"Sei {role}. Rispondi alla seguente domanda:\n{question}"

def ask_model(prompt_func, question):
    prompt = prompt_func(question)
    
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ], "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response

PROMPT_STRATEGIES = {
    "zero-shot": zero_shot_prompt,
    "few-shot": few_shot_prompt,
    "cot": cot_prompt,
    "react": react_prompt,
    "tree-of-thought": tree_of_thought_prompt,
    "generated-knowledge": generated_knowledge_prompt,
    "iterative-refinement": iterative_refinement_prompt,
    "self-consistency": self_consistency_prompt,
    "role-prompting": role_prompting_prompt,
}


if __name__ == "__main__":
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    print("Strategie di prompting disponibili:")
    for key in PROMPT_STRATEGIES:
        print(f"- {key}")

    prompt_strategy = input("\nScegli una strategia di prompting: ").strip().lower()
    question = input("Inserisci la tua domanda: ").strip()

    try:
        prompt_func = PROMPT_STRATEGIES[prompt_strategy]
        print(prompt_func)
        response = ask_model(prompt_func, question)
        
        print(f"Response status code: {response.status_code}\n")
        print(response.json()["choices"][0]["message"]["content"])

    except KeyError:
        print(f"Strategia '{prompt_strategy}' non riconosciuta.")
    except Exception as e:
        print(f"Errore durante la chiamata al modello: {prompt_strategy}")

