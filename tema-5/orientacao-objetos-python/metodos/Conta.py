#Toda classe precisa possuir um conjunto de métodos para manipular os atributos e, por consequência, o estado do objeto. 
#Por exemplo, precisamos depositar dinheiro na conta para aumentar o valor da conta corrente.

def depositar (self, valor):
     self.saldo += valor

#No código, foi definido um método depositar, que recebe a própria instância do objeto por meio do self e de um parâmetro valor. O número passado por intermédio do parâmetro será adicionado ao saldo da conta do cliente.
#Vamos supor que o estado anterior do objeto representasse o saldo com o valor zero da conta. Após a chamada desse método, passando como parâmetro o valor 300, o estado da conta foi alterado com o novo saldo de 300 reais graças à referência self.

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo): #Método construtor
         self.numero = numero
         self.cpf = cpf
         self.nomeTitular = nomeTitular
         self.saldo = saldo

    def depositar(self, valor):
         self.saldo += valor

    def sacar(self, valor):
         self.saldo -= valor

#No exemplo, adicionamos mais um método sacar(self, valor), do qual subtraímos o valor, passado como parâmetro, do saldo do cliente. Pode ser adicionado um método extrato para avaliar os valores atuais da conta corrente, ou seja, o estado atual do objeto.
#A conta tinha, por exemplo, um saldo de 300 reais após o primeiro depósito. Após a chamada de sacar (100), o saldo da conta será de 200 reais. Desse modo, se o método gerar_extrato() for executado, o valor impresso será 200.

    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf}\nsaldo: {self.saldo}")


def main():
    c1 = Conta(1,1,"Joao",0)
    c1.depositar(300)
    c1.sacar(100)
    c1.gerar_extrato()

if __name__ == "__main__": 
    main()