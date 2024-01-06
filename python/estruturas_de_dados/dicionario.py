pessoa = {"nome":"Aroldo","idade":39}
print(type(pessoa)) #<class 'dict'>
print(pessoa["idade"]) #39
pessoa["religiao"] = "cristao"
print(pessoa) #{'nome': 'Aroldo', 'idade': 39, 'religiao': 'cristao'}


perfumes = {
    "Dior Home Sport" : {"topo": ["limao","bergamota"],"coracao": ["Elemi","Pimenta Rosa"],"base":["Olibano","Ambar"]},
    "Armani Code Parfum" : {"topo": ["bergamota"],"coracao": ["Íris","Salvea"],"base":["Fava tonka","salvia"]}
}

print(perfumes)
print(perfumes["Dior Home Sport"]["coracao"][0]) #Elemi

for chave, valor in perfumes.items():
    print(chave, valor)


print("\n\n##### metodos ######\n\n")
#copy
perfumes_2 = perfumes.copy()
#print(perfumes_2)

#clear
perfumes_2.clear()
#print(perfumes_2)

#fromkeys , cria dicionario com conjunto de chaves no dicionário com valor none ou um valor default
perfumes_3 = dict.fromkeys(["ferrari black","acqua di gio"],"teste")
print(perfumes_3) #{'ferrari black': 'teste', 'acqua di gio': 'teste'}

#get , nao da erro quando é passado uma chave que nao existe 
print(perfumes_3.get("ferrari black")) #teste
print(perfumes_3.get("nao existe")) #None

#items , retorna uma lista de tuplas com chave e valor
print(perfumes_3.items()) #dict_items([('ferrari black', 'teste'), ('acqua di gio', 'teste')])

#keys , retorna lista de chaves
print(perfumes.keys()) #dict_keys(['Dior Home Sport', 'Armani Code Parfum'])

#values , retorna lista com todos os valores do dicionário
print(perfumes.values()) 

#pop , remove uma chave informado como parametro do dicionário , o valor removido é retornado    
print(perfumes_3.pop("acqua di gio"))
print(perfumes_3)
    
#setdefault , se a chave existe nao insere e retorna a atual , se nao existe insere ela
print(perfumes_3.setdefault("ferrari black","teste2"))
print(perfumes_3)
print(perfumes_3.setdefault('acqua di gio', 'teste'))    
print(perfumes_3)

#update ,se a chave existe ele insere , se nao existe insere ela
print(perfumes_3.update({"ferrari black":"teste2"}))
print(perfumes_3)
    
#popitem, remove chave sequencialmente
print(perfumes_3.popitem())
print(perfumes_3)
    
#in , verifica se uma chave existe no dicionário
print("ferrari black" in perfumes_3)   

#del , remove valores ou toda a chave
del perfumes_3["ferrari black"]
print(perfumes_3)
