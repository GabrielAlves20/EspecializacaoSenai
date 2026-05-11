mensagemUsuario = input("Digite uma mensagem: ")

arquivoChatbot = open("chatbot.txt", "w")

arquivoChatbot.write(mensagemUsuario)

arquivoChatbot.close()