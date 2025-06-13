print(f"Calculadora de Combustível\n")
etanol = float(input('Digite o valor do etanol: ').replace(",", "."))
gasolina = float(input('Digite o valor da gasolina: ').replace(",", "."))



while True:
    if etanol <= 0:
        print("Valores inválidos. Insira valores positivos para etanol e gasolina.")
    elif gasolina <= 0:
        print("Valores inválidos. Insira valores positivos para etanol e gasolina.")
        

    razao = etanol / gasolina
    if razao < 0.7:
        print("É melhor abastecer com etanol.")
    else:
        print("É melhor abastecer com gasolina.")
    break

continua = int(input(f" Digite [1] para continuar ou [2] para terminar \n"))

if continua == 2:
    print("retorna o código.")
else:
    print("Terminou o código.")

   


