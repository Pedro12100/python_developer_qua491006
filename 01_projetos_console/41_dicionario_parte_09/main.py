import os 
os.system("cls")

usuarios = [
    {
        "nome": "Pedro",
        "idade": 18,
        "Email": "Fulano@gmail.com"
    },
    {
        "nome": "Joao",
        "idade": 40,
        "Email": "Joao@gmail.com"
    },
    {
        "nome": "Maria",
        "idade": 20,
        "Email": "Maria@gmail.com"
    },
    {
        "nome": "Jose ",
        "idade": 80,
        "Email": "Jose@gmail.com"
    }
]

# exibe os dados 
for usuario in usuarios:
    print("-"*40)
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")

















