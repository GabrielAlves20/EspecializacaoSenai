nomeUsuario = input("Digite o nome do usuário: ")

arquivo = open("usuarios.txt", "w")

arquivo.write(nomeUsuario)

arquivo.close()