palavrasBoas = 0
palavrasGerais = ""

while True:
    palavrasGerais = input("Digite qualquer palavra: (Digite >tchau< para sair)")
    if palavrasGerais.lower() in ["bom", "ótimo"]:
        palavrasBoas += 1

    elif palavrasGerais.lower() == "tchau":
        print(f"sistema encerrado, você digitou {palavrasBoas} palavras boas")
        break