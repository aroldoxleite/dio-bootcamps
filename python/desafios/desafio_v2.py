


saldo = 0.0
extrato = ""
limite_valor = 500
limite_qtd = 3
AGENCIA = "0001"

usuarios = {}
contas = {}

def menu():
   menu = """
      Selecione uma opção:
   
      (1) - Depositar
      (2) - Sacar
      (3) - Exibir extrato
      (4) - Criar usuário
      (5) - Criar conta
      (6) - Exibir usuarios
      (7) - Exibir contas
      (8) - Sair
   """
   return int(input(menu))

def sacar(*,limite_qtd,limite_valor,saldo,valor,extrato):

   if limite_qtd != 0:
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

   return saldo,extrato,limite_qtd

def depositar(valor,saldo,extrato,/):
   if valor <= 0 :
      print("Valor inválido")
   else:
      saldo += valor
      extrato += f"\nDeposito R$ {valor:.2f}"

   return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
   print("########## EXTRATO ##########")
   print("\nNão foram realizadas movimentações" if not extrato else extrato)
   print(f"Saldo R$ {saldo:.2f}\n")
   print("#############################")

def cadastrar_usuario(usuarios):
 
   cpf = input("Informe o CPF (somente numeros): ")

   if cpf in usuarios:
      print("cpf ja existe!")
   else:
      nome = input("Informe o nome: ")
      data_nascimento = input("informe data nascimento: ")
      endereco = input("informe endereço: ")

      usuarios[cpf] = {"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco,"cpf":cpf}

def cadastrar_conta(AGENCIA,contas,usuarios):
   cpf = input("Informe o cpf do cliente (somente numeros): ")

   if cpf in usuarios:
      numero_conta = len(contas)+1
      contas[numero_conta] = {"conta":numero_conta,"agencia":AGENCIA,"usuario":usuarios[cpf]}
   else:
      print("Usuário não existe")

def exibir_usuarios(usuarios):
   print(usuarios)

def exibir_contas(contas):
   print(contas)

def main():
   while True:

      opcao = menu()

      if opcao == 1:
         valor = float(input("Informe o valor do depósito: "))
         saldo,extrato= depositar(valor,saldo,extrato)   
      elif opcao == 2:
         valor = float(input("Informe o valor do saque: "))
         saldo,extrato,limite_qtd = sacar(limite_qtd=limite_qtd,limite_valor=limite_valor,saldo=saldo,extrato=extrato,valor=valor)
      elif opcao == 3:
         exibir_extrato(saldo,extrato=extrato)
      elif opcao == 4:
         cadastrar_usuario(usuarios)
      elif opcao == 5:
         cadastrar_conta(AGENCIA,contas,usuarios)
      elif opcao == 6:
         exibir_usuarios(usuarios)
      elif opcao == 7:
         exibir_contas(contas)
      elif opcao == 8:
         break
      else:
         print("Opção inválida")

main()


    