import os 
os.system("cls") 

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: ").replace(",","."))

#Estrutura de decisão
if idade >= 12 and altura >= 1.15:
    print(f"{nome} está autorizado a entrar.")
else:
     print(f"{nome} não foi autorizado a entrar.")




