import requests

POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_data(pokemon_name):
    response = requests.get(f"{POKEAPI_URL}{pokemon_name}")
    return response.json()