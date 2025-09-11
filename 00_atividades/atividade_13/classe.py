import json
class Conta:
    # construtor
    def __init__(self, titular, cpf, agencia, conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    # Metodos da classe Conta
    def consultar_dados(self):
        print(f"Agência: {self.agencia}.")
        print(f"Conta: {self.conta}.")
        print(f"Saldo: R$ {self.saldo:.2f}.")



    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    


    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def imprimir_extrato(self):
        dados = {
            "Nome do titular": self.titular,
            "CPF do titular": self.cpf,
            "Agência": self.agencia,
            "Conta": self.conta,
            "Saldo": self.saldo
        }

        with open("Conta.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
       