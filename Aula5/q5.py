pergunta = input("Digite sua pergunta: ")

arquivo = open("historico_ia.txt", "a")

arquivo.write(pergunta + "\n")

arquivo.close()

print("Pergunta salva com sucesso!")