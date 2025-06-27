import os 
os.system("cls")

usuario = {
    "nome" : "Pedro Henrique",
    "idade" : 40,
    "email" : "pbastos435@gmail.com",
    "profissão" : "programador"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-"*40)

# usuário informa a chave que deseja excluir
chave = input("informe a chave que deseja excluir: ").lower().strip()

# verifica se a chave existe
if chave in usuario:
    # excluir a chave
    del usuario[chave]
else:
    print("Chave inexistente") 


print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")