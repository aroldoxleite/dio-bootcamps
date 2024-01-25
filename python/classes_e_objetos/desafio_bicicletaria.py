class Bicicleta:

    def __init__(self,cor,modelo,ano,valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim Plim")

    
    def parar(self):
        print("Parando....")
              

    def correr(self):
        print("Vrummm")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("azul","speed",2020,1000.00)
b1.buzinar()
b1.correr()
b1.parar()
print(b1)

