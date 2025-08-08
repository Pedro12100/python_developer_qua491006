from abc import ABC
from abc import abstractmethod

# classe abstrata
class Conta(ABC):
    @abstractmethod
    def __init__(self, titular, cpf, agencia, numero_conta, saldo):
        # atributos private
        self.__saldo = saldo

    # métodos get e set
        @property
        def saldo(self):
            return self.__saldo

        @saldo.setter
        def saldo(self, saldo):
            self.__saldo = saldo 


        # métodos de ação
        @abstractmethod
        def consultar_dados(self):
            pass

        @abstractmethod
        def depositar(self, valor):
            pass

        @abstractmethod
        def sacar(self, valor):
            pass

class ContaCorrente(Conta): 
    def __init__(self, titular, cpf, agencia, numero_conta, conta, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia 
        self.__conta = conta
        super().__init__(saldo)        


    @property
    def titular(self):
        return self.__titular 
    
    @titular.setter
    def titular(self, titular):
        self.__titular

    @property
    def cpf(self):
        return self.cpf 
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf

    @property
    def agencia(self):
        return self.agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia

    @property
    def conta(self):
        return self.conta
    
    @conta.setter
    def conta(self, conta):
        self.__conta

    # métodos da interface
    def consultar_dados(self):
        print(f"{"-"*20} DADOS DA CONTA {"-"*20}\n")
        print(f"Titular da conta: {self.__titular}")
        print(f" CPF do titular: {self.__cpf}")
        print(f"Agência: {self.__agencia}")
        print(f"Número da conta: {self.__conta}")
        print(f"Saldo: R$ {self.__saldo:.2f}")

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def sacar(self, valor):
        self.__saldo -= valor
        return self.__saldo






    
