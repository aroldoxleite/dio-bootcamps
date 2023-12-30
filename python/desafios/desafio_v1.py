
menu = """
   Selecione uma opção:
   
   (1) - Depositar
   (2) - Sacar
   (3) - Exibir extrato
   (4) - Sair

"""

saldo = 0.0
extrato = ""
limite_valor = 500
limite_qtd = 3


while True:

   opcao = int(input(menu))

   if opcao == 1:
      #depositar
      valor = float(input("Informe o valor do depósito: "))
      
      if valor <= 0 :
         print("Valor inválido")
      else:
         saldo += valor
         extrato += f"\nDeposito R$ {valor:.2f}"
      

   elif opcao == 2:

      #sacar
      if limite_qtd != 0:
         valor = float(input("Informe o valor do saque: "))
   
         if valor > saldo:
            print("Saldo indisponível")
         elif valor > limite_valor:
            print("Valor maior que limite de por saque")
         else:
            saldo -= valor
            extrato += f"\nSaque R$ {valor:.2f}"
            limite_qtd -= 1
      else:
         print("Limite de saques diário atingido")

   elif opcao == 3:

      #Exibir extrato
      print("########## EXTRATO ##########")
      print("\nNão foram realizadas movimentações" if not extrato else extrato)
      print(f"Saldo R$ {saldo:.2f}\n")
      print("#############################")

   elif opcao == 4:
      break
   else:
      print("Opção inválida")


    