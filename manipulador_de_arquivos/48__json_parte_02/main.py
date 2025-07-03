import json
import os
os.system("cls")

try:
    arquivo = input("Informe o arquivo: ").strip().lower()

    # tenta ler a lista de pessoas
    try:
        with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
            pessoas = json.load(f)
    except FileNotFoundError:
        pessoas = []

    nova_pessoa = {}

    nova_pessoa["nome"] = input("Informe o nome: ").strip().title()
    nova_pessoa["idade"] = int(input("Informe a sua idade: ").strip())
    nova_pessoa["cpf"] = input("Informe o CPF: ").strip()
    nova_pessoa["rg"] = input("Informe o RG: ").strip()
    nova_pessoa["data_nasc"] = input("Informe a data de nascimento: ").strip()
    nova_pessoa["sexo"] = input("Informe o sexo: ").strip()
    nova_pessoa["signo"] = input("Informe o signo: ").strip().capitalize()
    nova_pessoa["mãe"] = input("Informe o nome da mãe: ").strip().title()
    nova_pessoa["pai"] = input("Informe o nome do pai: ").strip().title()
    nova_pessoa["email"] = input("Informe o email: ").strip().lower()
    nova_pessoa["senha"] = input("Informe a senha: ")
    nova_pessoa["cep"] = input("Informe o CEP: ").strip()
    nova_pessoa["endereço"] = input("Informe o endereço: ").strip().title()
    nova_pessoa["numero"] = int(input("Informe o número do endereço: "))
    nova_pessoa["bairro"] = input("Informe o bairro: ").strip().capitalize()
    nova_pessoa["cidade"] = input("Informe a cidade: ").strip().title()
    nova_pessoa["estado"] = input("Informe o estado: ").strip().upper()
    nova_pessoa["telefone_fixo"] = input("Informe o telefone: ").strip()
    nova_pessoa["celular"] = input("Informe o celular: ").strip()
    nova_pessoa["altura"] = float(input("Informe a altura: ").replace(",", "."))
    nova_pessoa["peso"] = float(input("Informe o peso: ").replace(",", "."))
    nova_pessoa["tipo_sanguineo"] = input("Informe o tipo sanguíneo: ").strip().capitalize()
    nova_pessoa["cor"] = input("Informe a cor favorita: ").strip()

    pessoas.append(nova_pessoa)

    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(pessoas, f, ensure_ascii=False, indent=4)

    print(f"\n{'-'*20} LISTA DE PESSOAS {'-'*20}")
    for pessoa in pessoas:
        for chave in pessoa:
            print(f"{chave.capitalize()}: {pessoa[chave]}")
        print("-"*40)

except Exception as e:
    print(f"Não foi possível inserir pessoa. {e}.")
