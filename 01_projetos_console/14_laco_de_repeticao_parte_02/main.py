import os
os.system('cls' if os.name == 'nt' else 'clear')

# loop infinito
# ...existing code...
while True:
    # menu
    print(f"{'-' * 20} MENU {'-' * 20}\n")
    print("0 - Encerrar o programa")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")          
    print("4 - divisão")
    print(f"{'-' * 50}\n")

    Operador = input("Digite o número da operação: ").strip()

    match Operador:
        case "0":
            print("Programa encerrado.")
            break
        case "1":
            try:
                x = float(input("Informe o valor de x: ").replace(',', '.'))
                y = float(input("Informe o valor de y: ").replace(',', '.'))

                print(f"A soma de {x} + {y} = {x + y}")
            except Exception as e:
                print(f"Não foi possivel somar. {e}.")
            finally:
                continue
        case "2":
            try:
                x = float(input("Informe o valor de x: ").replace(',', '.'))
                y = float(input("Informe o valor de y: ").replace(',', '.'))

                print(f"A soma de {x} + {y} = {x + y}")
            except Exception as e:
                print(f"Não foi possivel somar. {e}.")
            finally:
                continue
        case "3":
            try:
                x = float(input("Informe o valor de x: ").replace(',', '.'))
                y = float(input("Informe o valor de y: ").replace(',', '.'))

                print(f"A soma de {x} + {y} = {x + y}")
            except Exception as e:
                print(f"Não foi possivel somar. {e}.")
            finally:
                continue  
        case "4":
            try:
                x = float(input("Informe o valor de x: ").replace(',', '.'))
                y = float(input("Informe o valor de y: ").replace(',', '.'))

                print(f"A soma de {x} + {y} = {x + y}")
            except Exception as e:
                print(f"Não foi possivel somar. {e}.")
            finally:
                continue
        case _:
            print("Operador inválido.")
            continue
            
