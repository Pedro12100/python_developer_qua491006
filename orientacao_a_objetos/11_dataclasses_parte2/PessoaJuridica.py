import Pessoa
from dataclasses import dataclass

@dataclass
class PessoaJuridica(Pessoa.Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str

    def __str__(self):
        separador = "-" * 20
        return (
            f"{separador} Dados da empresa: {separador}\n\n"
            f"Razão Social: {self.razao_social}\n"
            f"Nome da empresa: {self.nome_fantasia}\n"
            f"CNPJ: {self.cnpj}\n"
            f"E-mail: {self.email}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}"
        )
