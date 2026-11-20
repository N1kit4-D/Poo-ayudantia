import requests 

respuesta = requests.get(
    "https://openlibrary.org/search.json",
    timeout=(3,5)
)
print("Estado HTTP:", respuesta.status_code)
if respuesta.status_code == 200:
    result = respuesta.json()

print ("Que libro Buscas?: ")

