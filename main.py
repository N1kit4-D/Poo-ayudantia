import requests


respuesta = requests.get(
    "https://pokeapi.co/api/v2/pokemon",
    timeout=(3,5)
)

print("Estado HTTP:", respuesta.status_code)
if respuesta.status_code == 200:
    result = respuesta.json()


input("Ingrese nombre del pokemon: ")