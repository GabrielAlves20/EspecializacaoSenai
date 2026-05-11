comentarioUsuario = input("Digite um comentário: ")
arquivo = open("sentimentos.txt", "w")

if comentarioUsuario.lower() in ["bom", "ótimo"]:
    arquivo.write("O comentário é positivo")
    

elif comentarioUsuario.lower() in ["ruim", "péssimo"]:
    arquivo.write("O comentário é negativo")

arquivo.close()