acessos = open("acessos.txt", "w" )
acessos.write("Gabriel\nJoão\nJoaquina\nCirilo")
acessos.close()

nomeDoUsuario = input("Digite o seu nome: ")
acessos = open("acessos.txt", "a")
acessos.write(f"\n{nomeDoUsuario}")