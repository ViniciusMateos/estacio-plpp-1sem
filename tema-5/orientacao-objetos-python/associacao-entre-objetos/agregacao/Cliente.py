    #AGREGAÇÃO
        #Para atender a novas necessidades do sistema de conta corrente do banco, agora é necessário adicionar uma funcionalidade para o gerenciamento de conta conjunta, ou seja, uma conta corrente pode ter um conjunto de clientes associados.
        #Isso pode ser representado como uma agregação

class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco