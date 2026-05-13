import json

ia = {
    "pergunta": "O que é Inteligência Artificial?",
    "resposta": "É uma tecnologia capaz de simular inteligência humana."
}

jsonFake = json.dumps(ia, indent=4)

print(jsonFake)