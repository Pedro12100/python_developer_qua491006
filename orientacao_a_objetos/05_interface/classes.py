from abc import ABC, abstractmethod

# Classe abstrata
class Conta(ABC):
    def __init__(self, titular, cpf, agencia, numero_conta, saldo):
        self._titular = titular
        self._cpf = cpf
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass


# Classe concreta
class ContaCorrente(Conta):
    def __init__(self, titular, cpf, agencia, numero_conta, saldo):
        super().__init__(titular, cpf, agencia, numero_conta, saldo)

    def consultar_dados(self):
        print(f"{'-'*20} DADOS DA CONTA {'-'*20}")
        print(f"Titular da conta: {self._titular}")
        print(f" CPF do titular: {self._cpf}")
        print(f"Agência: {self._agencia}")
        print(f"Número da conta: {self._numero_conta}")
        print(f"Saldo: R$ {self._saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saque inválido ou saldo insuficiente.")
