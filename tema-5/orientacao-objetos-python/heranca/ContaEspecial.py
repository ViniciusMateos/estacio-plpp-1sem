#Herança é um dos princípios mais importantes da programação orientada a objetos
#pois permite a reutilização de código com a possiblidade de extensão para se ajustar às regras de negócio dos sistemas.

#Imagine que a área de produtos de um banco define quais clientes podem ter acesso a um produto chamado Conta especial
#que visa atender quem possui conta na instituição há mais de um ano. 
#Na visão de negócios, a conta especial possui a funcionalidade de permitir o saque até um certo limite
#que é determinado na criação da conta. Nesse ponto, há um dos grandes ganhos da orientação a objetos.

#O objeto do mundo real conta especial será mapeado para uma classe ContaEspecial, a qual, por sua vez, herdará todo código de conta

from Conta import Conta
import datetime

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f"Não existe saldo suficiente conta numero {self.numero} cliente {self.clientes.cpf}")
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True
        

#Método construtor __init__-
    #A classe tem de ser instanciada com a passagem do limite como um parâmetro da construção do objeto. 
    # O método __Init__ foi sobrescrito da superclasse Conta.
    #Já o método super(), que foi utilizado para chamar um método da superclasse, pode ser usado em qualquer método da subclasse 
    # A orientação a objetos permite inclusive a reutilização do construtor da classe pai (linha 16).

#Atributo limite
    #Adicionado apenas na subclasse ContaEspecial, em que ele será utilizado para implementar a regra de saques além do valor do saldo (linha 17).

#Método sacar()
    #O método precisa verificar se o valor a ser sacado, passado como parâmetro, é menor que a soma do saldo atual mais o limite da conta especial.
    #Nesse caso, a classe Conta Especial reescreveu o método sacar da superclasse Conta. Essa característica é conhecida como sobrescrita (override) dos métodos (linha 19).