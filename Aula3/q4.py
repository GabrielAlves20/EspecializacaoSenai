dados = open("dados.txt", "w" )
dados.write("Hello world!! ")
dados.close()

dados = open("dados.txt", "r" )
conteudo = dados.read()

print(conteudo)

