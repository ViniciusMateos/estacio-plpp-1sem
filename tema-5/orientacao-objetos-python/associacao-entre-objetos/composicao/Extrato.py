#A classe Conta ainda não está completa de acordo com as necessidades do sistema de conta corrente do banco. 
#Isso ocorre porque o banco precisa gerar extratos contendo o histórico de todas as operações realizadas para conta corrente.
#Para isso, o sistema precisa ser atualizado para adicionar uma composição de cada conta com o histórico de operações realizadas. 

#A classe Extrato tem as responsabilidades de armazenar todas as transações realizadas na conta e de conseguir imprimir um extrato com a lista dessas transações.

class Extrato:
    def __init__(self):
        self.transacoes = []


    def extrato(self, numeroconta):
        print(f"Extrato: {numeroconta} \n")
        for p in self.transacoes:
            print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")