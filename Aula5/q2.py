palavra = input("Digite uma palavra: ")

if palavra == "bom" or palavra == "feliz" or palavra == "ótimo":
    sentimento = "Positivo"

elif palavra == "ruim" or palavra == "triste" or palavra == "péssimo":
    sentimento = "Negativo"

else:
    sentimento = "Neutro"

print("Sentimento identificado:", sentimento)