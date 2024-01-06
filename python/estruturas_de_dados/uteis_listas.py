
#append
#adicao de elementos em uma lista
lista = []
lista.append(1)
lista.append("Aroldo")
lista.append([1,"dois",True])

print(lista)

#clear
lista.clear()
print(lista) #retorna lista vazia []

#copy
#retorna uma cópia do objeto lista em outra posicao de memoria
lista = [1,2,3]
lista2 = lista
lista2[0] = 4
print(lista)
print(lista2)
lista3 = lista.copy()
lista3[0] = 5
print(lista)
print(lista2)
print(lista3)

#count
#contar quantas vezes um objeto aparece dentro da lista
lista = ["Azul","Vermelho","Branco","Azul"]
print(lista.count("Preto")) #0
print(lista.count("Azul")) #2

#extend
#concatena duas listas
filmes = ["Esqueceram de mim","peter pan"]
filmes_nacionais = ["O auto da compadecida","Os trapalhoes"]

filmes.extend(filmes_nacionais)
print(filmes) #['Esqueceram de mim', 'peter pan', 'O auto da compadecida', 'Os trapalhoes']

#index
#retorna o indice da primeira ocorrencia do elemento
carros = ["punto","brasilia","fusca"]
print(carros.index("brasilia")) #1

#pop
#remove os elementos tirando os ultimos adicionando
linguagens = ["pascal","cobol","python"]
print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.pop()
print(linguagens)

#remove
#remove a primeira ocorrencia do elemento especifico
pratos_preferidos = ["pizza","parmegiana","pequi","parmegiana"]
pratos_preferidos.remove("parmegiana") 
print(pratos_preferidos) #['pizza', 'pequi', 'parmegiana']

#reverse
#cria um espelhamento da lista
restaurantes = ["barolo","purê","liro chef"]
restaurantes.reverse()
print(restaurantes) #['liro chef', 'purê', 'barolo']



#sort
#ordenacao padrao
restaurantes = ["barolo","purê","liro chef"]
restaurantes.sort()
print(restaurantes) #['barolo', 'liro chef', 'purê']
#ordenacao padrao invertida
restaurantes.sort(reverse=True)
print(restaurantes) #['purê', 'liro chef', 'barolo']
#ordenacao personalizada
restaurantes.sort(key=lambda x : len(x)) #ordenando pelo tamanho
print(restaurantes) #['purê', 'barolo', 'liro chef']
#ordenacao personalizada invertiva
restaurantes.sort(key=lambda x : len(x), reverse=True) #ordenando pelo tamanho inverso
print(restaurantes) #['liro chef', 'barolo', 'purê']



#len
#tamanho da lista
restaurantes = ["barolo","purê","liro chef"]
print(len(restaurantes)) #3

#sorted
#ordenar iteraveis
restaurantes = ["barolo","purê","liro chef"]
print(sorted(restaurantes)) #['barolo', 'liro chef', 'purê']
#ordenacao padrao invertida
print(sorted(restaurantes,reverse=True)) #['purê', 'liro chef', 'barolo']
#ordenacao personalizada
print(sorted(restaurantes,key=lambda x : len(x))) #['purê', 'barolo', 'liro chef']
#ordenacao personalizada invertiva
print(sorted(restaurantes,key=lambda x : len(x), reverse=True)) #['liro chef', 'barolo', 'purê']

