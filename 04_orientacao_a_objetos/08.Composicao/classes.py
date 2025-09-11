# Classe Pessoa
class Pessoa:
    def __init__(self, nome, cpf, email, telefone, endereco):
        self.__nome = nome 
        self.__cpf = cpf 
        self.__email = email 
        self.__telefone = telefone 
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, valor):
        self.__telefone = valor

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, valor):
        self.__endereco = valor

    def obter_dados(self):
        return (
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"Email: {self.email}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}\n"
        )


# Classe Veiculo
class Veiculo:
    def __init__(self, modelo, fabricante, cor, placa, ano, proprietario):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__cor = cor
        self.__placa = placa 
        self.__ano = ano
        self.__proprietario = proprietario 

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self.__fabricante = valor

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, valor):
        self.__cor = valor

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        self.__placa = valor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor):
        self.__ano = valor

    @property
    def proprietario(self):
        return self.__proprietario

    @proprietario.setter
    def proprietario(self, valor):
        self.__proprietario = valor

    def info_proprietario(self):
        return (
            f"Modelo: {self.modelo}\n"
            f"Fabricante: {self.fabricante}\n"
            f"Cor: {self.cor}\n"
            f"Placa: {self.placa}\n"
            f"Ano: {self.ano}\n"
            f"Proprietário: {self.proprietario.nome}\n"
        )
