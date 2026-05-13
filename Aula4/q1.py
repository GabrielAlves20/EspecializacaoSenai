import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

resposta = requests.get(url)

print(f"A cotação do dólar está atualmente em: R${resposta.json()["USDBRL"]["bid"]}")