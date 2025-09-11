import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="", idade=0)

    print(usuario)
    print(f"Idade: {len(usuario)}")



    del(usuario)

    print(usuario)


if __name__ == "__main__":
    main()