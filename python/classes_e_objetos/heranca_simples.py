class Veiculo:

    def __init__(self,cor,placa,nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas

    def ligar(self):
        print("Ligando motor")

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):

    def __init__(self,cor,placa,nro_rodas,carregado):
        self.carregado = carregado
        super().__init__(cor,placa,nro_rodas)

carro = Carro("Azul", "1111", 4)
carro.ligar()

moto = Moto("Branco", "2222", 2)
moto.ligar()

caminhao = Caminhao("Preto" , "3333", 8, True)
caminhao.ligar()



