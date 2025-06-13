import os
os.system("cls")

# tratamento de exceção
try:
    n = int(input('Digite um número: '))
    print(f'Você digitou o número {n}')
except Exception as e:
    print(f'Não foi possível realizar a operação. {e}')
finally:
    print("Programa encerrado com sucesso.")