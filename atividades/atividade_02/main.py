import math
import os

while True:
    print(f"{'-' * 20} MENU {'-' * 20}\n")
    print("1 - Calcular área de um circulo")
    print("2 - Calcular tamanho de uma circunferência")
    print("3 - Sair do programa")
    opcao = input("Informe sua opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    
    try:
        if opcao == "1" or opcao == "2":
            raio = float(input("Informe o valor do raio: ").replace(',', '.'))
        else:
            pass
            os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                area = math.pi * (raio ** 2)
                print(f"Área do círculo: {area}.")
            case "2":
                circunferencia = 2 * math.pi * raio
                print(f"Tamanho da circunferência: {circunferencia}.")
            case _:
                print(f"Opção inválida.")
    except ValueError as e:
        print(f"Não foi possível calcular. {e}.")
