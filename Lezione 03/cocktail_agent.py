def get_cocktail_recipe(name):
    recipes = {
        "Piña Colada": {
            "ingredienti": [
                "60ml (2 oz) Rum Bianco",
                "90ml (3 oz) Succo d'Ananas",
                "30ml (1 oz) Latte di Cocco"
            ],
            "preparazione": "Frullare tutti gli ingredienti con ghiaccio fino ad ottenere una consistenza cremosa. Servire in un bicchiere hurricane e guarnire con una fetta di ananas e una ciliegina.",
            "difficoltà": "Facile",
            "bicchiere": "Hurricane glass"
        },
        "Whiskey Sour": {
            "ingredienti": [
                "60ml (2 oz) Whiskey",
                "22ml (3/4 oz) Succo di Limone fresco",
                "15ml (1/2 oz) Sciroppo di Zucchero",
                "1 Albume d'uovo (opzionale)"
            ],
            "preparazione": "Shakerare energicamente tutti gli ingredienti con ghiaccio. Filtrare in un bicchiere old fashioned con ghiaccio. Guarnire con una fetta di limone e una ciliegina al maraschino.",
            "difficoltà": "Media",
            "bicchiere": "Old fashioned"
        },
        "Mai Tai": {
            "ingredienti": [
                "30ml (1 oz) Rum Bianco",
                "30ml (1 oz) Rum Scuro",
                "15ml (1/2 oz) Succo di Lime fresco",
                "15ml (1/2 oz) Sciroppo di Orzata",
                "15ml (1/2 oz) Triple Sec o Cointreau"
            ],
            "preparazione": "Shakerare tutti gli ingredienti con ghiaccio. Versare in un bicchiere riempito con ghiaccio tritato. Guarnire con una fetta di lime e un rametto di menta.",
            "difficoltà": "Media",
            "bicchiere": "Tumbler alto"
        },
        "Spritz": {
            "ingredienti": [
                "90ml (3 oz) Prosecco",
                "60ml (2 oz) Aperol",
                "30ml (1 oz) Soda o acqua frizzante",
                "Ghiaccio"
            ],
            "preparazione": "Riempire un bicchiere con ghiaccio. Versare prima il Prosecco, poi l'Aperol e infine la soda. Mescolare delicatamente. Guarnire con una fetta d'arancia.",
            "difficoltà": "Facile",
            "bicchiere": "Calice da vino"
        },
        "Moscow Mule": {
            "ingredienti": [
                "60ml (2 oz) Vodka",
                "120ml (4 oz) Ginger Beer",
                "15ml (0.5 oz) Succo di Lime fresco"
            ],
            "preparazione": "Riempire una tazza di rame con ghiaccio. Aggiungere la vodka e il succo di lime. Completare con ginger beer e mescolare delicatamente. Guarnire con una fetta di lime e un rametto di menta (opzionale).",
            "difficoltà": "Facile",
            "bicchiere": "Tazza di rame"
        },
        "Caipirinha": {
            "ingredienti": [
                "60ml (2 oz) Cachaça",
                "1 Lime intero, tagliato a spicchi",
                "2 cucchiaini di Zucchero bianco"
            ],
            "preparazione": "Tagliare il lime a spicchi e metterlo in un bicchiere basso con lo zucchero. Pestare energicamente per estrarre il succo e gli oli essenziali. Aggiungere ghiaccio tritato e Cachaça. Mescolare bene.",
            "difficoltà": "Facile",
            "bicchiere": "Old fashioned"
        },
        "Mojito": {
            "ingredienti": [
                "60ml (2 oz) Rum bianco",
                "30ml (1 oz) Succo di lime fresco",
                "2 cucchiaini di Zucchero bianco",
                "6-8 foglie di Menta fresca",
                "Soda o acqua frizzante"
            ],
            "preparazione": "Mettere le foglie di menta, lo zucchero e il succo di lime in un bicchiere alto. Pestare delicatamente per rilasciare gli oli della menta. Aggiungere ghiaccio tritato e rum. Completare con soda e mescolare. Guarnire con un rametto di menta e una fetta di lime.",
            "difficoltà": "Media",
            "bicchiere": "Collins"
        },
        "Negroni": {
            "ingredienti": [
                "30ml (1 oz) Gin",
                "30ml (1 oz) Campari",
                "30ml (1 oz) Vermouth rosso"
            ],
            "preparazione": "Mescolare tutti gli ingredienti direttamente in un bicchiere con ghiaccio. Guarnire con una scorzetta d'arancia.",
            "difficoltà": "Facile",
            "bicchiere": "Old fashioned"
        }
    }
    
    if name in recipes:
        return format_recipe(name, recipes[name])
    else:
        # Corrispondenze parziali
        for cocktail_name in recipes:
            if name.lower() in cocktail_name.lower():
                return format_recipe(cocktail_name, recipes[cocktail_name])
        
        # Suggerimenti se non troviamo il cocktail
        return get_not_found_message(name, recipes.keys())

def format_recipe(name, recipe_details):
    formatted = f"\n===== {name.upper()} =====\n"
    formatted += f"\nBicchiere: {recipe_details['bicchiere']}\n"
    formatted += f"Difficoltà: {recipe_details['difficoltà']}\n"
    
    formatted += "\nINGREDIENTI:\n"
    for ingredient in recipe_details["ingredienti"]:
        formatted += f"\t• {ingredient}\n"
    
    formatted += "\nPREPARAZIONE:\n"
    formatted += f"{recipe_details['preparazione']}\n"
    
    return formatted

def get_not_found_message(query, available_cocktails):
    message = f"Mi dispiace, non conosco la ricetta per '{query}'.\n\n"
    message += "Ecco i cocktail che conosco:\n"
    
    for cocktail in sorted(available_cocktails):
        message += f"• {cocktail}\n"
        
    message += "\nProva a inserire il nome esatto di uno di questi cocktail."
    return message

def main():
    print("\n===== BARMAN VIRTUALE =====")
    print("Inserisci il nome di un cocktail per vedere la ricetta.")
    print("Scrivi 'lista' per vedere tutti i cocktail disponibili.")
    print("Scrivi 'esci' per terminare il programma.\n")
    
    while True:
        cocktail = input("Inserisci il nome del cocktail: ").strip()
        
        if cocktail.lower() == 'esci':
            print("\nGrazie per aver usato il Barman Virtuale! Arrivederci! 🍸")
            break
            
        elif cocktail.lower() == 'lista':
            print("\nCocktail disponibili:")
            recipes = {
                "Piña Colada": {}, "Whiskey Sour": {}, "Mai Tai": {}, 
                "Spritz": {}, "Moscow Mule": {}, "Caipirinha": {},
                "Mojito": {}, "Negroni": {}
            }
            for idx, name in enumerate(sorted(recipes.keys()), 0):
                print(f"{idx}. {name}")
            print()
            
        else:
            result = get_cocktail_recipe(cocktail)
            print(result)

if __name__ == "__main__":
    main()