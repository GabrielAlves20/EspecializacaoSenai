inputCliente = ""

while True:
    inputCliente = input("")
    if inputCliente.lower() == "oi":
        print("Olá! Como posso ajudar? ")
    elif inputCliente.lower() == "tchau":
        print("Sistema encerrado! ")
        break
    else:
        print("Não entendi sua mensagem")

     

