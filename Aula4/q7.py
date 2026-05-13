import json

pergunta = input("Digite uma pergunta: ")

chatbot = {
    "pergunta": pergunta,
    "resposta": "Sei la"
}

dados_json = json.dumps(chatbot, indent=4)

print(dados_json)