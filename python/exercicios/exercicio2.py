T = int(input())
resto = 0
for i in range(T):
  valores = input().split()

  garrafas_cheias = int(valores[0]) #7
  garrafas_vazias_para_premio = int(valores[1]) #4
  
  premio_dia_sem_resto = garrafas_cheias // garrafas_vazias_para_premio
  resto = garrafas_cheias % garrafas_vazias_para_premio
  premio_total = premio_dia_sem_resto + resto
  print(premio_total)
