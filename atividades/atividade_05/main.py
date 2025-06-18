"""
TODO - atividade: Crie um programa que recebe do usuário o nome e a idade, e em seguida, mostre um menu de filmes com suas respectivas classificações.
indicativas e salas de exibição. Exemplo:
- Sala 1: A Roda Quadrada - livre 
- Sala 2: A volta dos que não foram - 12 anos
- Sala 3: Poeira em alto Mar - 14 anos
- Sala 4: As tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos

O usuário deve escolher a sala que está passando o filme que deseja assistir.
- Se o usuário tiver a idade minima ou mais para ver o filme, o programa
imprime o ingresso com o nome do usuário, a sala, o nome do filme, a data e a 
hora da compra do ingresso, e deseje bom filme , e em seguida, encerra o programa.
- Se o usuário não tiver a idade minima para ver o filme, o program bloqueia
a sua entrada, e re-exibe o menu de filmes para que ele escolha outro filme.

"""
import os
os.system("cls" if os.name == "nt" else "clear")

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print("\nEscolha um filme:")
print("- Sala 1: A Roda Quadrada - livre")
print("- Sala 2: A volta dos que não foram - 12 anos")
print("- Sala 3: Poeira em alto Mar - 14 anos")
print("- Sala 4: As tranças do Rei Careca - 16 anos")
print("- Sala 5: A Vingança do Peixe Frito - 18 anos")
sala = input("Digite o número da sala que deseja assistir: ")

if sala == "1":
    filme = "A Roda Quadrada"
    mensagem = "Bom filme!"
    print(f"Seu ingresso foi solicitado com sucesso {nome} {filme} na sala{sala}. {mensagem}.")
else:
    print("Você não tem idade suficiente para assistir a este filme.")    










































"""
from datetime import date

hoje = date.today().strftime("%d/%m/%Y")
print(hoje)

"""