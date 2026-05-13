import requests

url = "https://restcountries.com/v3.1/name/brazil"

resposta = requests.get(url)

dados = resposta.json()

pais = dados[0]["name"]["common"]
capital = dados[0]["capital"][0]
populacao = dados[0]["population"]

print(f"País: {pais}")
print(f"Capital: {capital}")
print(f"População: {populacao}")