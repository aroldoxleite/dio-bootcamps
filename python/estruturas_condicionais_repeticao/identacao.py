def sacar(valor):
    saldo = 500
    if(saldo >= valor):
        saldo -= valor
        print("Valor sacado")
        print("Retire o dinheiro")

    print(f"Finalizado, saldo atual: {saldo}")


def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Finalizado, saldo atual: {saldo}")

depositar(100)
sacar(200)