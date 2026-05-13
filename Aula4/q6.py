import requests
import json

url = "https://api.github.com"

resposta = requests.get(url)

dados = resposta.json()

arquivo = open("dados_api.json", "w")

json.dump(dados, arquivo, indent=4)

arquivo.close()

print("Dados salvos em dados_api.json")