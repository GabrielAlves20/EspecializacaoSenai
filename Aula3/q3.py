usuarioNota1 = int(input("Digite a primeira nota: "))

usuarioNota2 = int(input("Digite a segunda nota: "))

arquivo = open("notas.txt", "w")

arquivo.write(f"nota 1: {usuarioNota1} nota 2: {usuarioNota2}")

arquivo.close()