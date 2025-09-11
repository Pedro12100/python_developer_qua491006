import PessoaFisica
import PessoaJuridica


def main():
    usuario = PessoaFisica.PessoaFisica(
    email="", telefone="", endereco="", nome="", cpf="", idade=0
    )
    empresa = PessoaJuridica.PessoaJuridica(
        email="", telefone="", endereco="", razao_social="", nome_fantasia="", cnpj=""
    )

    # input
    print("Informe os dados do usuário:\n")
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = (input("Informe seu CPF: ")).strip()
    usuario.idade = int(input("Informe sua idade: "))
    usuario.email = input("Informe seu email: ").strip().lower()
    usuario.telefone = input("Informe seu telefone: ").strip()
    usuario.endereco = input("Informe seu endereco: ").strip()

  
    print("Informe os dados da empresa:\n")
    empresa.razao_social = input("Informe a razão social: ").strip()
    empresa.nome_fantasia = input("Informe o nome da empresa : ").strip()
    empresa.cnpj = input("Informe seu CNPJ: ").strip()
    empresa.email = input("Informe seu email: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip()

  

    # output
    print(usuario)
    print(empresa)


    if __name__ == "__main__":
        main()

