from deep_translator import GoogleTranslator
import os 

limpar = lambda: os.system("cls")


def main():
    tradutor = GoogleTranslator(source="auto", target="en")

    while True:
        try:
            print("1 - Traduzir texto.")
            print("2 - Sair do programa.")
            opcao = input("Informe a opção desejada: ").strip()
            match opcao:
                case "1":
                    texo_original = input("Digite o texto a ser traduzido: ")
                    texto_traduzido = tradutor.translate(texo_original)
                    print(f"Texto traduzido:\n{texto_traduzido}")
                case "2":
                    print("Programa encerrado")
                    break
                case _:
                    print("Opção inválida.")
                    continue
        except Exception as e:
            print(f"Não foi possível traduzir. {e}.")
            continue

if __name__ == "__main__":
    main()



