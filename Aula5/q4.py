import json

dados = {
    "pergunta": "O que é Inteligência Artificial?",
    "resposta": "IA é uma tecnologia capaz de simular inteligência humana."
}

json_formatado = json.dumps(dados, indent=4, ensure_ascii=False)

print(json_formatado)