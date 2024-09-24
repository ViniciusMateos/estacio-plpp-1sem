from Cliente import Cliente
from Conta import Conta

cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente ("456", "Maria", "Rua W")
conta1 = Conta([cliente1, cliente2], 1, 2000)
conta1.depositar(1000)
conta1.sacar(1500)
conta1.extrato.extrato(conta1.numero)
print(f"SALDO: {conta1.saldo}")

# As duas primeiras linhas importam as definições das classes necessárias para criar clientes e contas.

# As próximas duas linhas criam instâncias da classe Cliente, cada uma com um CPF, nome e endereço específicos. Dois clientes são criados: o cliente1 Joao com CPF "123" e o cliente2 Maria com CPF "456".

# A linha seguinte cria uma instância da classe Conta, que associa os clientes criados anteriormente a uma conta bancária específica com um saldo inicial. Uma conta (conta1) é criada com o número 1, associada aos clientes Joao e Maria, com um saldo inicial de 2000.

# As linhas seguintes realizam um depósito e um saque na conta criada, atualizando o saldo e registrando as transações no extrato. Um depósito de 1000 é realizado na conta, aumentando o saldo para 3000. A transação de depósito é registrada no extrato.

# Depois, um saque de 1500 é realizado na conta, diminuindo o saldo para 1500. A transação de saque é registrada no extrato.

# A última linha chama o método para exibir o extrato da conta, mostrando todas as transações realizadas até o momento.