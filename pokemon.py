import requests
import json

def fetch_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    print(f"Status code for {name}: {response.status_code}")
    if response.status_code == 200:
        raw_json = response.json()
        # print("Raw JSON:")
        # print(json.dumps(raw_json, indent=4))
        print("\nFiltered Output:")
        print("Name:", raw_json['name'])
        print("Height:", raw_json['height'])
        print("Weight:", raw_json['weight'])
    else:
        print("Error fetching data")

# Dynamic fetch (success example - user input)
pokemon_name = input("Enter a valid Pokémon name (e.g., pikachu): ")
fetch_pokemon(pokemon_name)
