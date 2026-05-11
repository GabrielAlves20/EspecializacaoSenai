import random
arquivo = open("recomendacoes.txt", "w")

filmes = [
    ["John Wick", "Mad Max", "Velozes e Furiosos"],   # ação
    ["Invocação do Mal", "It", "Annabelle"],          # terror
    ["As Branquelas", "Shrek", "Gente Grande"]        # comédia
]

generoDoFilme = ""

while generoDoFilme not in ["acao", "terror", "comedia"]:
    escolher = int(input("Escolha o genero do filme: \n1 - Ação\n2 - Terror\n3 - comédia\n"))
    if escolher == int(1):
        generoDoFilme = "acao"
        filme = random.choice(filmes[0])
        arquivo.write(f"Filme recomendado para você: {filme}")


        
    elif escolher == 2:
        generoDoFilme = "terror"
        filme = random.choice(filmes[1])
        arquivo.write(f"Filme recomendado para você: {filme}")

    elif escolher == 3:
        generoDoFilme = "comedia"
        filme = random.choice(filmes[2])
        arquivo.write(f"Filme recomendado para você: {filme}")

arquivo.close()
