class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaconta(self, conta_cliente):
        self.contas.append(conta_cliente)

    def calcularrendimentomensal(self):
        for c in self.contas:
            c.calculoRendimento()

    def imprimesaldocontas(self):
        for c in self.contas:
            c.extrato()