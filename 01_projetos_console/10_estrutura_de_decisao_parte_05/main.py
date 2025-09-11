import os
os.system("cls")

# Declaração de variáveis
x = float(input("Informe o valor de x: ").replace(",", "."))
y = float(input("Informe o valor de y: ").replace(",", "."))

# Menu
print(f"{'-'*20} ESCOLHA A OPERAÇÃO {'-'*20}\n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operador = input("Informe a operação desejada: ").strip() # ELEMINA A PORRA DE ESPAÇOS NO INÍCIO E NO FIM


# Match case para operações
match operador:
    case "1":
        print(f"A soma dos valores é {x + y}.")
    case "2":
        print(f"A subtração dos valores é {x - y}.")
    case "3":
        print(f"A multiplicação dos valores é {x * y}.")
    case "4":
        if y == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            print(f"A divisão dos valores é {x / y}.")
    case _:
        print("Erro: Operação inválida! Por favor, escolha uma das opções do menu.")



