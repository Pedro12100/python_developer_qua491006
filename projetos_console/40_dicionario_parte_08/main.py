import os
os.system("cls")

chaves = ("Nome", "Idade", "E-mail" , "Telefone", "Profissão")
usuario = {
    chaves[0]: "Pedro Bastos",
    chaves[1]: 40,
    chaves[2]: "phbastos@gmail",
    chaves[3]: "(90) 123456-7894",
    chaves[4]: "empresario",
   
}

for chave in chaves:
    print(f"{chave}: {usuario.get(chave)}")