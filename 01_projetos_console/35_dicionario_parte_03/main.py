import os
os.system("cls")


usuario = {
     "nome": "Alex",
    "idade": 18,
    "email": "alex@gmail.com",
    "profissão": "DBA"
}

for chave in usuario:
    print(f"{chave.capitalize()} : {usuario.get(chave)}")