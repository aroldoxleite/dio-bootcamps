while True:
    opcao = int(input("Digite um numero :"))
    if not opcao % 2:
        continue # interrompe o laço e vai para a próxima iteracao
        print("nao vai ser impresso")
    else:
        break # interrompe o laço finalizando