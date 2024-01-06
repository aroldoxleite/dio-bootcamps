N = int(input())

while(N > 0):
  caso = input()
  numero_1,numero_2 = caso.split(" ")

  numero_1 = numero_1[(len(numero_1)-len(numero_2)):len(numero_1)]
  
  if numero_1 == numero_2 :
    print("encaixa")
  else:
    print("nao encaixa")
  
  N -= 1