cores_set_1 = {"azul","roxo","amarelo","roxo"}
cores_lista = ["azul","roxo","amarelo","roxo"]
print(cores_set_1) #{'roxo', 'amarelo', 'azul'}
print(cores_lista) #['azul', 'roxo', 'amarelo', 'roxo']
cores_set_2 = set(cores_lista)
print(cores_set_2) #{'amarelo', 'azul', 'roxo'}
print(type(cores_set_2)) #<class 'set'>



frutas_1 = {"limao","laranja","uva"}
frutas_2 = {"laranja","abacate","morango"}
frutas_3 = {"uva","limao"}

#union
print(frutas_1.union(frutas_2)) #{'laranja', 'limao', 'morango', 'uva', 'abacate'}

#intersection
print(frutas_1.intersection(frutas_2)) #{'laranja'}

#difference
print(frutas_1.difference(frutas_2)) #{'uva', 'limao'}

#symmetric difference
print(frutas_1.symmetric_difference(frutas_2)) #{'limao', 'morango', 'uva', 'abacate'}

#issubset subconjunto
print(frutas_3.issubset(frutas_1)) #True
print(frutas_1.issubset(frutas_3)) #False

#issuperset
print(frutas_3.issuperset(frutas_1)) #False
print(frutas_1.issuperset(frutas_3)) #True

#isdisjoint ,se sao conjuntos diferentes
print(frutas_3.isdisjoint(frutas_2)) #True
print(frutas_2.isdisjoint(frutas_3)) #True

#add , se nao existir é adicionado
frutas_3.add("Pera")
print(frutas_3) #{'uva', 'limao', 'Pera'}

#copy
frutas_3_copy = frutas_3.copy()
print(frutas_3_copy) #{'uva', 'limao', 'Pera'}

#clear
frutas_3_copy.clear()
print(frutas_3_copy)

#discard se o elemento nao existir nao da erro
frutas_3.discard("Pera")
print(frutas_3)

#pop
print(frutas_3.pop())
print(frutas_3)

#remove se o elemento nao existe da um erro
frutas_3.remove("uva")
print(frutas_3)