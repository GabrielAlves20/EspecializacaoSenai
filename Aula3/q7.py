tarefa1 = input("Digite a primeira tarefa: ")
tarefa2 = input("Digite a segunda tarefa: ")
tarefa3 = input("Digite a terceira tarefa: ")

arquivo = open("tarefas.txt", "a")

arquivo.write(f"{tarefa1}\n{tarefa2}\n{tarefa3}")
