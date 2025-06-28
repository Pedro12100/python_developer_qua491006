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
import datetime
import random

os.system("cls" if os.name == "nt" else "clear")

usuarios = []

while True:
    print(f"\n{'-' * 20} MENU {'-' * 20}")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Alterar todos os usuários cadastrados")
    print("4 - Sortear usuário")
    print("5 - Excluir usuário sorteado")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    try:
        match opcao:
            case "1":
                nome = input("Digite o nome completo: ").strip()
                nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
                email = input("Digite o e-mail: ").strip()
                cpf = input("Digite o CPF: ").strip()
                telefone = input("Digite o telefone: ").strip()
                genero = input("Digite o gênero: ").strip()
                data_cadastro = datetime.date.today().strftime("%d/%m/%Y")
                hora_cadastro = datetime.datetime.now().strftime("%H:%M:%S")

                usuario = {
                    "Nome": nome,
                    "Nascimento": nascimento,
                    "Email": email,
                    "CPF": cpf,
                    "Telefone": telefone,
                    "Gênero": genero,
                    "Data do cadastro": data_cadastro,
                    "Hora do cadastro": hora_cadastro
                }

                usuarios.append(usuario)
                print("Usuário cadastrado com sucesso!")

            case "2":
                if not usuarios:
                    print("Nenhum usuário encontrado.")
                else:
                    print("\nLista de usuários:")
                    for u in usuarios:
                        print("\nUsuário:")
                        for chave, valor in u.items():
                            print(f"{chave}: {valor}")

            case "3":
                print("Função de alteração de usuários ainda não implementada.")

            case "4":
                if not usuarios:
                    print("Nenhum usuário para sortear.")
                else:
                    sorteado = random.choice(usuarios)
                    print("\nUsuário sorteado:")
                    for chave, valor in sorteado.items():
                        print(f"{chave}: {valor}")

            case "5":
                if not usuarios:
                    print("Nenhum usuário para excluir.")
                else:
                    sorteado = random.choice(usuarios)
                    usuarios.remove(sorteado)
                    print(f"Usuário '{sorteado['Nome']}' removido com sucesso.")

            case "6":
                print("Encerrando o programa...")
                break

            case _:
                print("Opção inválida. Tente novamente.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")











                   