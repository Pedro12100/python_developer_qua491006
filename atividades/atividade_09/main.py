"""
# TODO - atividade: Crie um programa que faça as seguintes funções:
- Cadastre um novo usuário;
- Liste todos os usuário;
- Altere todos os usuários cadastrados;
- Fazer sorteio de usuário;
- Exclua sorteio de usuário;
- Saia do programa;
# NOTE - dados do usuário:
- Nome completo; 
- Data de Nascimento;
- E-mail;
- CPF;
- Telefone;
- Gênero;
- Data do cadastro; (pegar do sistema)
- Hora do cadastro; (pegar do sistema)
"""

import os
import random
from datetime import date, datetime

# lista vazia
usuarios = []

# loop principal
while True:
    print(f"\n{'-' * 20} MENU {'-' * 20}")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Alterar todos os usuários cadastrados")
    print("4 - Sortear usuário")
    print("5 - Excluir usuário sorteado")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "1":
            try:
                novo_usuario = []
                novo_usuario["nome"] = input("Informe o nome: ").strip().title()
                novo_usuario["data de nascimento"] = input("Informe a data de nascimento: ").strip()
                novo_usuario["email"] = input("Informe o email: ").strip().lower()
                novo_usuario["cpf"] = input("Informe o CPF: ").strip()
                novo_usuario["telefone"] = input("Informe o telefone: ").strip()
                novo_usuario["genero"] = input("Informe o gênero: ").strip()
                novo_usuario["data do cadastro"] = date.today().strftime("%d/%m/%Y")
                novo_usuario["hora do cadastro"] = datetime.now().strftime("%H:%M:%S")

                usuarios.append(novo_usuario)
                os.system('cls' if os.name == 'nt' else 'clear')

                print(f'Usuário {novo_usuario.get("nome")} cadastrado com sucesso.')
            except Exception as e:
                print(f"Não foi possível cadastrar usuário. {e}")
            finally:
                continue

        case "2":
            try:
                if not usuarios:
                    print("Nenhum usuário cadastrado.")
                else:
                    for i, user in enumerate(usuarios):
                        print(f"Indice: {i}")
                        for chave, valor in user.items():
                            print(f"{chave.capitalize()}: {valor}")
                        print("-" * 40)
            except Exception as e:
                print(f"Não foi possível listar usuários. {e}.")
            finally:
                continue

        case "3":
            try:
                i = int(input("Informe o índice que deseja alterar: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                if 0 <= i < len(usuarios):
                    print(f'{"-"*20} Dados do usuário {"-"*20}')
                    for chave, valor in usuarios[i].items():
                        print(f"{chave.capitalize()}: {valor}")
                    print("\n")
                    while True:
                        chave_escolhida = input("Informe qual chave deseja alterar: ").strip().lower()
                        if chave_escolhida in usuarios[i]:
                            novo_valor = input(f"Informe o novo valor de {chave_escolhida}: ")
                            usuarios[i][chave_escolhida] = novo_valor
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Chave alterada com sucesso.")
                        else:
                            print("Chave inexistente.")
                        while True:
                            prosseguir = input("Deseja alterar outra chave? (s/n): ").strip().lower()
                            if prosseguir in ("s", "n"):
                                break
                        match prosseguir:
                            case "s":
                                continue
                            case "n":
                                break
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar dados; {e}.")
            finally:
                continue

        case "4":
            try:
                if len(usuarios) == 0:
                    print("Nenhum usuário cadastrado para sortear.")
                else:
                    i = random.randint(0, len(usuarios) - 1)
                    print("Usuário sorteado:")
                    for chave, valor in usuarios[i].items():
                        print(f"{chave.capitalize()}: {valor}")
            except Exception as e:
                print(f"Não foi possível sortear usuários. {e}.")
            finally:
                continue

        case "5":
            try:
                i = int(input("Informe o índice a ser excluído: "))
                if 0 <= i < len(usuarios):
                    for chave, valor in usuarios[i].items():
                        print(f"{chave.capitalize()}: {valor}")
                    while True:
                        excluir = input("Tem certeza? (s/n): ").strip().lower()
                        if excluir in ("s", "n"):
                            break
                        else:
                            print("Opção inválida.")
                    match excluir:
                        case "s":
                            del usuarios[i]
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Usuário excluído com sucesso.")
                        case "n":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Usuário não excluído.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível excluir usuário. {e}.")
            finally:
                continue

        case "6":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")
            continue
