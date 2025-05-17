import requests
import json
from typing import Dict, Optional

class OllamaTemplateGenerator:
    def __init__(self, base_url: str = "http://localhost:11434/api/generate", default_model: str = "llama3"):
        self.base_url = base_url
        self.default_model = default_model
        self.templates = {
            "ricetta": {
                "prompt": """Genera una ricetta {tipo} vegana con queste sezioni:
                                1. **Nome**: Nome creativo
                                2. **Ingredienti**: Lista in markdown
                                3. **Preparazione**: Passaggi numerati
                                4. **Variante**: Suggerimento per modificare
                                5. **Info**: Tempo e difficoltà

                                Focus su: {focus}""",
                                                "defaults": {"tipo": "principale", "focus": "ingredienti stagionali"}
                                            },
                                            "articolo": {
                                                "prompt": """Scrivi un breve articolo su {argomento} con:
                                - Introduzione coinvolgente
                                - 3 punti chiave
                                - Conclusione con call-to-action

                                Tono: {tono}""",
                "defaults": {"tono": "professionale"}
            }
        }

    def generate_text(
        self,
        template_name: str,
        variables: Optional[Dict] = None,
        model: Optional[str] = None,
        temperature: float = 0.7,
        stream: bool = False
    ) -> str:
        """Genera testo usando un template predefinito"""
        if template_name not in self.templates:
            raise ValueError(f"Template non trovato. Disponibili: {list(self.templates.keys())}")

        template = self.templates[template_name]
        # Unisce i default con le variabili fornite
        params = {**template["defaults"], **(variables or {})}
        prompt = template["prompt"].format(**params)

        payload = {
            "model": model or self.default_model,
            "prompt": prompt,
            "options": {"temperature": temperature},
            "stream": stream
        }

        try:
            response = requests.post(
                self.base_url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                timeout=60
            )
            response.raise_for_status()
            return response.json()["response"]
        
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Errore API Ollama: {str(e)}")
        except json.JSONDecodeError:
            raise ValueError("Risposta API non valida")

if __name__ == "__main__":
    generator = OllamaTemplateGenerator()
    
    try:
        print("=== RICETTA VEGANA ===")
        ricetta = generator.generate_text(
            "ricetta",
            {"tipo": "antipasto", "focus": "avocado e ceci"},
            temperature=0.8
        )
        print(ricetta)

        print("\n=== ARTICOLO ===")
        articolo = generator.generate_text(
            "articolo",
            {"argomento": "benefici della dieta vegana", "tono": "amichevole"}
        )
        print(articolo)

    except Exception as e:
        print(f"Errore: {str(e)}")