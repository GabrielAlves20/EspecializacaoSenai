import random

arquivo = open("recomendacoes.txt", "w")

filmes_acao = ["John Wick", "Mad Max", "Velozes e Furiosos"]
filmes_terror = ["Invocação do Mal", "It", "Annabelle"]
filmes_comedia = ["As Branquelas", "Shrek", "Gente Grande"]

genero = input(
    "Digite seu gênero favorito:\n"
    "acao\n"
    "terror\n"
    "comedia\n"
).lower()

if genero == "acao":
    filme = random.choice(filmes_acao)

elif genero == "terror":
    filme = random.choice(filmes_terror)

elif genero == "comedia":
    filme = random.choice(filmes_comedia)

else:
    filme = "Nenhum filme encontrado para esse gênero."

print("Filme recomendado:", filme)

arquivo.write(f"Filme recomendado: {filme}")

arquivo.close()