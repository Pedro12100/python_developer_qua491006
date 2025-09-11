import classes as c

def main():
    # Instancia objeto da classe ContaCorrente
    cc = c.ContaCorrente(
        titular="João Silva",
        cpf="123.456.789-00",
        agencia="1010-1",
        numero_conta="10101-1",
        saldo=0.0
    )

    print(f"Saldo inicial: R$ {cc.saldo:.2f}")
    
    cc.consultar_dados()

    cc.depositar(100)
    print(f"Saldo após depósito: R$ {cc.saldo:.2f}")

    cc.sacar(50)
    print(f"Saldo após saque: R$ {cc.saldo:.2f}")

if __name__ == "__main__":
    main()






