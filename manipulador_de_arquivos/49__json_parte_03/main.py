import json
import os
os.system("cls")  # Limpa a tela no Windows

try:
    arquivo = input("Informe o arquivo: ").strip().lower()

    # Abre para leitura
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        lista = json.load(f)

    for dado in lista:
        dado["altura"] = dado["altura"].replace(",", ".")
        dado["altura"] = float(dado["altura"])
        dado["peso"] = float(dado["peso"])

    # Abre para escrita
    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

    print("Conversão gravada com sucesso.")

except Exception as e:
    print(f"Não foi possível converter. {e}.")
