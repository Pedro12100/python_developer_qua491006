import modulo as mo 

if __name__ == '__main__':
    while True:
        print("1 - Calcular equação do 1º grau")
        print("2 - Calcular equação do 2º grau")
        print("3 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        match opcao:
            case "1":
                try:
                    a = float(input("Informe o valor de a: ").replace(',', '.'))
                    b = float(input("Informe o valor de b: ").replace(',', '.'))
                    x = mo.primeiro_grau(a, b)
                    print(f"O valor de x é: {x}")
                except Exception as e:
                    print(f"Erro. {e}")
                finally:
                    continue
            case "2":
                try:
                    a = float(input("Informe o valor de a: ")).replace((',', '.'))
                    b = float(input("Informe o valor de b: ")).replace((',', '.'))
                    c = float(input("Informe o valor de c: ")).replace((',', '.'))
                    x = mo.segundo_grau(a, b, c)
                    print(f"{x}.")
                except Exception as e:
                    print(f"Erro. {e}")
                finally:
                    continue
            case "3":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue