def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem_2(nome):
    print(f"Olá {nome}")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Olá {nome}")

exibir_mensagem() #Olá mundo
exibir_mensagem_2("Aroldo") #Olá Aroldo
exibir_mensagem_3("Aroldo") #Olá Aroldo
exibir_mensagem_3() #Olá Anônimo

########################################

def calcula_total(numeros):
    return sum(numeros)

def mostra_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor , sucessor

print(calcula_total([1,2,3])) #6
print(mostra_antecessor_sucessor(10)) #(9,11)

########################################

def salvar_carro(nome,modelo,marca,ano):
    print(f"Salvando carro {nome}/{modelo}/{marca}/{ano}")

salvar_carro("Gol","G5","WV",2010)
salvar_carro(modelo="G5",ano=2010,marca="WV",nome="Gol")
salvar_carro(**{"modelo":"G5","ano":2010,"marca":"WV","nome":"Gol"})
salvar_carro(*["Gol","G5","WV",2010])

#######################################

def mensagem_argumento_tupla (*texto):
    print(type(texto))
    print(texto)

def mensagem_argumento_dict (**texto):
    print(type(texto))
    print(texto)

mensagem_argumento_tupla("mensagem teste","mensagem 2")
mensagem_argumento_dict(chave1="mensagem teste",chave2="mensagem 2")

def mensagem_argumento_dupla_dict ( *args, **kwargs):
    print(type(args)) #<class 'tuple'>
    print(args) #('mensagem teste', 'mensagem 2')
    print(type(kwargs)) #<class 'dict'>
    print(kwargs) #{'chave1': 'mensagem teste', 'chave2': 'mensagem 2'}

mensagem_argumento_dupla_dict("mensagem teste","mensagem 2",chave1="mensagem teste",chave2="mensagem 2")

def somar(a , b):
    return a + b

def multiplicar(a ,b):
    return a * b

def exibir_mensagem_funcao(a , b , funcao):
    resultado = funcao(a,b)
    print(f"Resultado da operacao {funcao.__name__} com valores {a} , {b} é {resultado}")

exibir_mensagem_funcao(2,3,multiplicar)
exibir_mensagem_funcao(2,3,somar)

salario = 2000

def bonus(valor):
    salario += valor
    print(salario)

bonus(100)
print(salario)


    