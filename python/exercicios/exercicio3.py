a = input()
b = input()
c = input()

homem = ["vertebrado","mamifero","onivoro"]
aguia = ["vertebrado","ave","carnivoro"]
minhoca = ["vertebrado","anelidio","onivoro"]
pulga = ["invertebrado","inseto","hematofago"]
lagarta = ["invertebrado","inseto","herbivoro"]
sanguessuga = ["invertebrado","anelideo","hematofago"]

if a == homem[0] and b == homem[1] and c == homem[2]:
  print("homem")
elif a == aguia[0] and b == aguia[1] and c == aguia[2]:
  print("aguia")
elif a == pulga[0] and b == pulga[1] and c == pulga[2]:
  print("pulga")
elif a == sanguessuga[0] and b == sanguessuga[1] and c == sanguessuga[2]:
  print("sanguessuga")
elif a == lagarta[0] and b == lagarta[1] and c == lagarta[2]:
  print("lagarta")
else:
  print("minhoca")