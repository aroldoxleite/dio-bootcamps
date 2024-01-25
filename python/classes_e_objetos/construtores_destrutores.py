class Cachorro:

    def __init__(self, nome, cor, acordado=True):
        print("Inicializando classe")
        self.nome = nome
        self.nome = cor
        self.acordado = acordado

    def latir(self):
        print("uauuau")

    def __del__(self):
        print("rmovendo a instancia da classe")


cao = Cachorro("Belinha", "amarelo")
cao.latir()