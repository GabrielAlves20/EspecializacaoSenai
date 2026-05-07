soma = float(0)

for i in range(1, 6):
    notas = float(input(f"Digite a nota {i}: "))
    soma += notas
    
if (soma / 5) >= 7:
    print("Aprovado! ")

else:
    print("Reprovado")