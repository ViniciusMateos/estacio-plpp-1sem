from Cliente import Cliente
from Conta import Conta
from ContaEspecial import ContaEspecial

cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")
cliente3 = Cliente("789", "Joana", "Rua H")

#As três contas foram iniciadas, as contas comuns com saldo 2000 e a contaEspecial 1000
conta1 = Conta(cliente2, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaEspecial(cliente3, 3, 1000, 2000)

#impresso o saldo das três contas
print(f"Cliente: {cliente1.cpf} da conta comum {conta1.numero} possui saldo R$ {conta1.saldo}")
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R$ {conta2.saldo}")
print(f"Cliente: {cliente3.cpf} da conta especial {conta3.numero} possui saldo R$ {conta3.saldo} e limite R$ {conta3.limite}\n")

#depositou 500 e tentou sacar 3000 da conta comum que não terá saldo
conta2.depositar(500)
#mensagem indicando saldo após depósito
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R$ {conta2.saldo} \n")

conta2.sacar(3000)
#mensagem indicando que não foi possível sacar e o saldo atual
print(f"Cliente: {cliente2.cpf} da conta comum {conta2.numero} possui saldo R$ {conta2.saldo} \n")

#depositou 100 e tentou sacar 2000 da conta especial que tem limite
conta3.depositar(100)
#mensagem indicando saldo após depósito
print(f"Cliente: {cliente3.cpf} da conta especal {conta3.numero} possui saldo R$ {conta3.saldo} e limite {conta3.limite}\n")

conta3.sacar(2000)
#mensagem indicando que foi possível sacar e saldo negativo
print(f"Cliente: {cliente3.cpf} da conta especal {conta3.numero} possui saldo R$ {conta3.saldo} e limite {conta3.limite}\n")

#tentativa de saque acima do limite
conta3.sacar(2000)
print(f"Cliente: {cliente3.cpf} da conta comum {conta3.numero} possui saldo R$ {conta3.saldo} e limite R$ {conta3.limite}\n") 

#Vamos entender a execução do programa.

#O programa começa com a criação de três clientes: João (cliente1), Maria(cliente2) e Joana(cliente3). Cada cliente é identificado por seu CPF, nome e endereço.

# Em seguida, o programa cria três contas bancárias:

#     Conta1: Uma conta comum para João, com um saldo inicial de R$ 2000.
#     Conta2: Outra conta comum, desta vez para Maria, também com um saldo inicial de R$ 2000.
#     Conta3: Uma conta especial para Joana, que tem um saldo inicial de R$ 1000 e um limite de crédito adicional de R$ 2000.


# Exibição dos Saldos Iniciais
#     Antes de realizar qualquer transação, o programa imprime os saldos iniciais das três contas.
#     Essa ação permite que o usuário visualize o estado inicial de cada conta. 
#     Em particular, a conta especial de Joana é destacada por seu limite de crédito, além do saldo inicial.


# Operações Bancárias
#     A primeira operação realizada no programa é um depósito de R$ 500 na conta de Maria.
#     Este depósito é simples e direto, aumentando o saldo de Maria para R$ 2500.
#     Logo após, o programa tenta realizar um saque de R$ 3000 da mesma conta.

#     No entanto, como o saldo de Maria não é suficiente para cobrir esse saque, a operação falha.
#     O saldo permanece inalterado em R$ 2500, e o programa informa ao usuário que o saque não foi possível devido ao saldo insuficiente.

#     Na sequência, o programa foca na conta especial de Joana.
#     Primeiro, R$ 100 são depositados, elevando o saldo de Joana para R$ 1100. Em seguida, o programa realiza um saque de R$ 2000.
#     Como esse valor excede o saldo disponível, a conta entra no limite de crédito, resultando em um saldo negativo de R$ -900 e reduzindo o limite de crédito de Joana para R$ 1100. 
#     O sistema permite essa transação e atualiza os valores adequadamente, refletindo o uso do limite de crédito.

#     Finalmente, o programa tenta realizar um segundo saque de R$ 2000 na conta de Joana, que já está utilizando parte de seu limite.
#     Desta vez, o saque falha, pois o valor solicitado ultrapassa o limite de crédito restante.
#     O programa então exibe uma mensagem informando que a operação não pode ser concluída e mantém os valores do saldo e do limite inalterados.

#A ContaEspecial é uma classe comum e pode ser instanciada como todas as outras classes independentes da instanciação de objetos da classe Conta.