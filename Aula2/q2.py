comentarioUsuario = input("Digite um comentário: ")

if comentarioUsuario.lower() in ["bom", "ótimo"]:
    print("O comentário é positivo")

elif comentarioUsuario.lower() in ["ruim", "péssimo"]:
    print("O comentário é negativo")

else:
    print("O comentário é neutro")