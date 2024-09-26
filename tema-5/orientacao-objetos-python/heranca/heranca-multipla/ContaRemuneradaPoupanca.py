from Conta import Conta
from Poupanca import Poupanca

class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, taxa_remuneracao, clientes, numero, saldo):
        Conta.__init__(self, clientes, numero, saldo) #importando atributos da superclasse Conta
        Poupanca.__init__(self, taxa_remuneracao) #importando atributos da superclasse Poupanca 
        # Com a herança de duas classes distintas, faz com que seja uma herança múltipla

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaremuneracaoMes / 30)

#A linha 4 indica que a classe é herdeira de Conta e de Poupança (nessa ordem). Tal ordem tem importância, pois existem dois métodos no pai com o mesmo nome. 
#O Python dá prioridade para a primeira classe que implementa esse método na ordem da declaração

#Deve ser chamado o construtor explicitamente das superclasses com o seguinte formato:
    #nomeclasse.__init__(construtores). Isso pode ser visto nas linhas 6 e 7.