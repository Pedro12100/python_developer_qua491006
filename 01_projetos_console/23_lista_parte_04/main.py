import os 
os.system("cls") 

# lista
cidades = [
    "Brasília",
    "Goiania",
     "Curitiba",
     "Florianópolis",
    "Rio de Janeiro",
    "Brasília",
    "Teresina",
    "São Paulo",
    "Florianópolis",  
]


# usuário informa o nome da cidade a ser pesquisada
cidade_pesquisada = input("Informe o nome da cidade: ").title().strip()

# programa conta quantas vezes ocorre o item pesquisado
quantidade = cidades.count(cidade_pesquisada)

# programa indica quantas vezes o item foi encontrado
print(f"{cidade_pesquisada} foi encontrado {quantidade} vezes na lista.")
