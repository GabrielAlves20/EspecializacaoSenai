resposta = input("Digite sua resposta: ")

arquivo = open("respostas.txt", "a")

arquivo.write(resposta + "\n")

arquivo.close()

print("Resposta salva com sucesso!")