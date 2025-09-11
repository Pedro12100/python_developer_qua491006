from modulo import limpar_tela, velocidade_media, tempo_medio, aceleracao_media

v = None 

if __name__ == "__main__":
    while True:
        print("1 - Calcular Velocidade Média.")
        print("2 - Calcular aceleração média.")
        print("3 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        limpar_tela()
        match opcao:
            case '1':
                try:
                    vi = float(input("Informe a velocidade inicial: ").replace(',', '.'))
                    vf = float(input("Informe a velocidade final: ").replace(',', '.'))
                    v = velocidade_media(vi, vf)

                    limpar_tela()
                    print(f"A velocidade média é: {v} m/s")
                except Exception as e:
                    print(f"Erro: {e}")
                finally:
                    continue

            case '2':
                try:
                    t = float(input("Informe o tempo: ").replace(',', '.'))
                    if v is not None:
                        a = aceleracao_media(v, t)
                        print(f"A aceleração média é: {a}.")
                    else:
                        print("Velocidade média ainda não foi calculada.")
                    limpar_tela()
                except Exception as e:
                    print(f"Erro: {e}")
                finally:
                    continue

            case '3':
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue
