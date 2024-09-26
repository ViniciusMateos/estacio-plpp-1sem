from Cliente import Cliente
from Conta import Conta
from Poupanca import Poupanca
from ContaRemuneradaPoupanca import ContaRemuneradaPoupanca

cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")

conta1 = Conta([cliente1, cliente2], 1, 2000)
contapoupanca1 = Poupanca(0.1)
contaremunerada1 = ContaRemuneradaPoupanca(0.1, [cliente1], 5, 1000)

contaremunerada1.remuneraConta()
contaremunerada1.gerarsaldo()

#O programa cria dois clientes, João(cliente1) e Maria(cliente2), que são representados por objetos da classe Cliente.

# A seguir, o programa cria três tipos distintos de contas bancárias.
# A primeira conta, associada a João e Maria, é uma conta bancária tradicional (conta1) com um saldo inicial de R$ 2000.
# Essa conta é criada utilizando a classe Conta.

# Paralelamente, uma segunda conta é criada usando a classe Poupanca (contapoupanca1). 
# Esta conta é especial, pois é definida com uma taxa de remuneração mensal de 10%.
# Embora não seja diretamente associada a um cliente ou saldo inicial neste cenário, a criação da conta poupança serve para ilustrar como a remuneração pode ser aplicada a um saldo ao longo do tempo.

# A terceira conta, no entanto, é a mais interessante. 
# Criada para João (contaremunerada1), a ContaRemuneradaPoupanca combina as características de uma conta tradicional com os benefícios de uma conta poupança.
# Com um saldo inicial de R$ 1000 e uma taxa de remuneração de 10% ao mês, essa conta não só permite operações bancárias comuns, como também aplica uma remuneração diária ao saldo,
# destacando a flexibilidade e o poder da herança múltipla utilizada na definição da classe ContaRemuneradaPoupanca.

# Após a criação das contas, o programa aplica a remuneração à conta remunerada de poupança de João.
# O método remuneraConta é chamado, e o saldo de R$ 1000 é ajustado com a remuneração diária baseada na taxa mensal.

# Especificamente, a remuneração é calculada dividindo a taxa mensal por 30 dias, resultando em um acréscimo de aproximadamente R$ 3,33 ao saldo original.

# Finalmente, o programa exibe o saldo atualizado da conta remunerada de João. Após a aplicação da remuneração, o saldo da conta é apresentado como R$ 1003,33, confirmando que a remuneração foi corretamente aplicada.
