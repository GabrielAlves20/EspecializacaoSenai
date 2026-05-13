import json

json_texto = '''
{
    "nome": "Marcela Luz",
    "idade": 21
}
'''

dados = json.loads(json_texto)

print(f"Nome: {dados['nome']}")
print(f"Idade: {dados['idade']}")