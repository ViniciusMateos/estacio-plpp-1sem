#As properties são uma estratégia importante disponibilizada pelo Python para acessar e modificar atributos de forma controlada.
#Ao usar o decorador @property em métodos, você mantém os atributos como protegidos, permitindo que sejam acessados apenas por meio desses métodos decorados. 
#Isso garante que os atributos sejam manipulados de maneira segura e conforme as regras definidas na classe.

#Por exemplo, na classe Conta, o atributo privado saldo não pode ser acessado diretamente para leitura. Em vez disso, ele é acessado por meio de um método decorado com @property

@property
def saldo(self):
   return self._saldo

#Esse método permite acessar o valor do atributo saldo de forma controlada. 
#Quando você deseja permitir que o atributo saldo seja modificado, pode utilizar o decorador @<nomedometodo>.setter.
#Isso força que qualquer alteração no valor do atributo privado passe por esse método, onde é possível incluir validações ou outras regras de negócios.

@saldo.setter
def saldo(self, saldo):
    if (self.saldo < 0):
        print("saldo inválido")
    else:
        self._saldo = saldo

#Nesse caso, ao tentar modificar o saldo, o método verifica se o valor é negativo e, se for, impede a alteração e exibe uma mensagem de erro. Caso contrário, o saldo é atualizado.
#O uso de properties ajuda a garantir o encapsulamento em Python, permitindo que você controle como os atributos são acessados e modificados. 
#No entanto, é uma boa prática definir esses métodos somente se houver uma regra de negócios específica associada ao atributo. Se não houver, o acesso aos atributos pode ser feito diretamente, conforme definido na classe.

#Os properties ajudam a garantir o encapsulamento no Python.

class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print ("saldo inválido")
        else:
            self._saldo = saldo
            
def main():
    conta = Conta(1)
    conta.saldo = 200 # usando o @saldo.setter  #Caso o valor seja negativo o atributo privado poderá ser alterado comforme a property setter definido no método saldo.
    print(f'saldo da conta = {conta.saldo}') # usando o @property
    
if __name__ == "__main__":
    main()

