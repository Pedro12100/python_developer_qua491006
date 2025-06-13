import os
os.system("cls")

# Declaração de variáveis
nome = input("Informe o nome do aluno: ")
idade = int(input("Informe a idade do aluno: "))

# ternaria
result = " é maior de idade." if idade >= 18 else "é menor de idade."

# saída
print(f"{nome} {result}")        