#Em Python, não é obrigatório haver um comando para indicar quando o método deve ser finalizado. Porém, na orientação a objetos, é bastante comum, como é o caso da programação procedural, retornar um valor a partir da análise do estado do objeto.
#Conforme exemplificaremos a seguir, o saque de um valor maior do que o saldo atual do cliente não é permitido; portanto, retorna a resposta “False” para o objeto que está executando o saque.

class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo): #Método construtor
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
            
    def gerar_extrato(self):
        print(f"numero: {self.numero}\n cpf: {self.cpf}\nsaldo: {self.saldo}")     
        
def main():
    c1 = Conta(1,1,"Joao",0)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerar_extrato()
    print(f"O saque foi realizado? {saque}")
    

if __name__ == "__main__": 
    main()