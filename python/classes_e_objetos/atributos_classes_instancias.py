class Estudante:
    escola = "DIO"

    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
         return f"Nome: {self.nome} Numero: {self.numero} Escola: {self.escola}"

aluno1 = Estudante("Aroldo", 111)
aluno2 = Estudante("José", 222)
print(aluno1)
print(aluno2)

Estudante.escola = "Alura"
print(aluno1)
print(aluno2)