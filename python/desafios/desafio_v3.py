from abc import ABC , abstractmethod , abstractproperty

class Historico:

   def __init__(self):
      self._transacoes = []

   @property
   def transacoes(self):
      return self._transacoes
      
   def adicionar_transacao(self, transacao):
      self._transacoes.append(
         {
            "tipo" : transacao.__class__.__name__,
            "valor": transacao.valor
         }
      )

class Conta:

   def __init__(self,cliente,numero):
      self._saldo = 0.0
      self._numero = numero
      self._agencia = "0001"
      self._cliente = cliente
      self._historico = Historico()

   @property
   def saldo(self):
      return self._saldo
   
   @property
   def historico(self):
      return self._historico

   def sacar(self,valor):      
      if valor > self._saldo or valor <= 0:
         print("Saque falhou!")
         return False
      
      self._saldo -= valor
      print("Saque realizado com sucesso!")
      return True
   def __str__(self):
      return f"Conta: {self._numero} Dono: {self._cliente._nome}"
      
   def depositar(self,valor):
      if valor <= 0 :
         print("Deposito falhou!")
         return False
  
      self._saldo += valor
      print("Deposito realizado com sucesso!")
      return True
      
   @classmethod
   def nova_conta(cls,cliente,numero):
      return cls(cliente,numero)

class ContaCorrente(Conta):

   def __init__(self, cliente, numero, limite=500.0,limite_saques=3):
      self._limite = limite
      self._limite_saques = limite_saques
      super().__init__(cliente,numero)

   def sacar(self, valor):
      if valor > self._limite or self._limite_saques == 0:
         print("Saque falhou!")
         return False
      
      self._limite_saques -= 1 
      return super().sacar(valor)

class Transacao(ABC):

   @property
   @abstractproperty
   def valor(self):
      pass

   @abstractmethod
   def registrar(self,conta):
      pass

class Saque(Transacao):

   def __init__(self,valor):
      self._valor = valor

   @property
   def valor(self):
      return self._valor

   def registrar(self,conta):
      if conta.sacar(self.valor):
         conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
   def __init__(self,valor):
      self._valor = valor

   @property
   def valor(self):
      return self._valor

   def registrar(self,conta):
      if conta.depositar(self.valor):
         conta.historico.adicionar_transacao(self)

class Cliente:
   def  __init__(self,endereco):
      self._endereco = endereco
      self._contas = []

   def realizar_transacao(self, conta, transacao):
      transacao.registrar(conta)

   def adicionar_conta(self, conta):
      self._contas.append(conta)

   @property
   def contas(self):
      return self._contas

class PessoaFisica(Cliente):
   def __init__(self, endereco, cpf, nome, data_nascimento):
      self._cpf = cpf
      self._nome = nome
      self._data_nascimento = data_nascimento
      super().__init__(endereco)

   @property
   def cpf(self):
      return self._cpf

   def __str__(self):
      return f"Nome: {self._nome} CPF: {self._cpf}"

def menu():
   menu = """
      Selecione uma opção:
   
      (1) - Depositar
      (2) - Sacar
      (3) - Exibir extrato
      (4) - Cadastrar cliente
      (5) - Cadastrar conta
      (6) - Exibir usuarios
      (7) - Exibir contas
      (8) - Sair
   """
   return int(input(menu))

def sacar(clientes):
   cpf = input("Informe o CPF do cliente(somente números): ")
   cliente = filtrar_cliente(cpf, clientes)

   if cliente:

      conta = recuperar_conta_cliente(cliente)

      if conta:
         valor = float(input("Informe o valor do saque: "))
         transacao = Saque(valor)
         cliente.realizar_transacao(conta,transacao)
      else:
         print("Conta nao encontrada para o cliente")
         return
   else:
      print("Cliente nao encontrado")

def depositar(clientes):
   cpf = input("Informe o CPF do cliente(somente números): ")
   cliente = filtrar_cliente(cpf, clientes)

   if cliente:

      conta = recuperar_conta_cliente(cliente)

      if conta:
         valor = float(input("Informe o valor do depósito: "))
         transacao = Deposito(valor)
         cliente.realizar_transacao(conta,transacao)
      else:
         print("Conta nao encontrada para o cliente")
         return
   else:
      print("Cliente nao encontrado")

def exibir_extrato(clientes):
   extrato = ""
   cpf = input("Informe o CPF do cliente: ")
   cliente = filtrar_cliente(cpf, clientes)
   if cliente:
      conta = recuperar_conta_cliente(cliente)
      if conta:
         transacoes = conta.historico.transacoes
         if transacoes:
            for transacao in transacoes:
               extrato += f"\n{transacao['tipo']}: {transacao['valor']:.2f}\n"
         else:
            extrato = "Não foram encontradas movimentações"
      else:
         print("Conta nao encontrada para o cliente")
         return
   else:
      print("Cliente nao encontrado")
      return

   print("########## EXTRATO ##########")
   print(extrato)
   print(f"Saldo R$ {conta.saldo:.2f}\n")
   print("#############################")

def cadastrar_cliente(clientes):
 
   cpf = input("Informe o CPF (somente números): ")

   cliente = filtrar_cliente(cpf, clientes)

   if cliente:
      print("cpf já existe!")
   else:
      nome = input("Informe o nome: ")
      data_nascimento = input("informe data nascimento: ")
      endereco = input("informe endereço: ")

      cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
      clientes.append(cliente)
      print("Cliente cadastrado com sucesso!")

def cadastrar_conta(contas,clientes):
   cpf = input("Informe o cpf do cliente (somente numeros): ")

   cliente = filtrar_cliente(cpf, clientes)

   if cliente:
      conta = ContaCorrente(cliente,len(contas)+1)
      contas.append(conta)
      cliente.adicionar_conta(conta)
      print("Conta criada com sucesso!")
   else:
      print("Cliente não encontrado")

def exibir_contas(contas):
   if contas:
      for conta in contas:
         print(conta)
   else:
      print("Sem contas cadastradas")

def exibir_clientes(clientes):
   if clientes:
      for cliente in clientes:
         print(cliente)
   else:
      print("Sem clientes cadastrados")

def filtrar_cliente(cpf,clientes):
   for cliente in clientes:
      if cliente.cpf == cpf:
            return cliente
      return None

def recuperar_conta_cliente(cliente):  
   if cliente.contas:
      return cliente.contas[0]
   return None

def main():
   clientes = []
   contas = []

   while True:

      opcao = menu()

      if opcao == 1:
         depositar(clientes)
      elif opcao == 2:
         sacar(clientes)
      elif opcao == 3:
         exibir_extrato(clientes)
      elif opcao == 4:
         cadastrar_cliente(clientes)
      elif opcao == 5:
         cadastrar_conta(contas,clientes)
      elif opcao == 6:
         exibir_clientes(clientes)
      elif opcao == 7:
         exibir_contas(contas)
      elif opcao == 8:
         break
      else:
         print("Opção inválida")


main()
