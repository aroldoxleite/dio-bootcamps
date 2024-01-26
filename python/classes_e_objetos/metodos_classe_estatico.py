class Pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def cria_pessoa(cls,nome,idade):
        return cls(nome,idade)
    
    @staticmethod
    def eh_de_maior(idade):
        return True if idade >= 18 else False


pessoa = Pessoa.cria_pessoa("Aroldo", 9)
print(pessoa.nome,pessoa.idade)
print("Eh de maior" if Pessoa.eh_de_maior(pessoa.idade) else "Menor de idade")