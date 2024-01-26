class Ave:
    def voar(self): pass

class Gaivota(Ave):
    def voar(self):
        print("Gaivota voa")

class Galinha(Ave):
    def voar(self):
        print("Galinha nao voa")

def plano_de_voo(self, passaro):
    passaro.voar() 

plano_de_voo(Gaivota())
plano_de_voo(Galinha())
