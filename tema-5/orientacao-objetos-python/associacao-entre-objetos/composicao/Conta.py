#A classe Conta possui todas as transações, como sacar, depositar e transfereValor. 
# Cada transação realizada deve adicionar uma linha ao extrato da conta.

#A composição Conta->Extrato inclusive precisa ser inicializada no construtor da classe Conta
#No construtor de Extrato, foi adicionado um atributo transações, o qual foi inicializado para receber um array de valores – transações da conta.


import datetime
from Extrato import Extrato

class Conta:
   def __init__(self, clientes, numero, saldo):
      self.clientes = clientes
      self.numero = numero
      self.saldo = saldo
      self.dataabertura = datetime.datetime.today()
      self.extrato = Extrato() #adição da função extrato dento do construtor da conta (composição)

   def depositar(self, valor):
      self.saldo += valor
      self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()]) #adição para enviar para o objeto Extrato ppor meio do atributo Extrato adicionado no construtor Conta. COm o objetivo de fazer um registro dentro do extrato a cada transação.

   def sacar(self, valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()]) #adição para enviar para o objeto Extrato ppor meio do atributo Extrato adicionado no construtor Conta. COm o objetivo de fazer um registro dentro do extrato a cada transação.
         return True

   def transfereValor(self, contaDestino, valor):
      if self.saldo < valor:
         return ("Não existe saldo suficiente")
      else:
         contaDestino.depositar(valor)
         self.saldo -= valor
         self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()]) #adição para enviar para o objeto Extrato ppor meio do atributo Extrato adicionado no construtor Conta. COm o objetivo de fazer um registro dentro do extrato a cada transação.
         return("Transferencia Realizada")

   def gerarsaldo(self):
      print(f"numero: {self.numero}\nsaldo: {self.saldo}")