# verifica se objetos estao presentes em uma sequencia

curso = "Curso Python"
frutas = ["laranja","uva","limão"]
saques = [1500,100]

print("Python" in curso) #true
print("Maçã" not in frutas) #true
print(200 in saques) #false
print(100 in saques) #false
print("100" in saques) #true