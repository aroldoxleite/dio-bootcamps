MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Informe sua idade: "))

# if idade >= MAIOR_IDADE:
#     print("Pode tirar CNH")

# if idade < MAIOR_IDADE:
#     print("Ainda nao pode tirar CNH")



# if idade >= MAIOR_IDADE:
#     print("Pode tirar CNH")
# else:
#     print("Ainda nao pode tirar CNH")


if idade >= MAIOR_IDADE:
    print("Pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Iniciar o treinamento")
else:
    print("Ainda nao pode tirar CNH")