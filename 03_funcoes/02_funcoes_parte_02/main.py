# função 
def mostrar_msg(nome):
    return f"Seja bem vindo, {nome}!"

# programa principal 
nome = input("Digite seu nome: ").strip().title()
print(mostrar_msg(nome))