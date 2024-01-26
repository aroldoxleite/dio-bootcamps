from abc import ABC , abstractmethod, abstractproperty

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):

    def ligar(self):
        print("Ligando TV")

    def desligar(self):
        print("Desligando TV")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):

    def ligar(self):
        print("Ligando AR")

    def desligar(self):
        print("Desligando AR")

    @property
    def marca(self):
        return "Samsumg"

ctr_tv = ControleTv()
ctr_tv.ligar()
print(ctr_tv.marca)

ctr_ar = ControleArCondicionado()
ctr_ar.ligar()
print(ctr_ar.marca)