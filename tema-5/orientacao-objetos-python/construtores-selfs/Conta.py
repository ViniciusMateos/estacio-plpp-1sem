#A classe Conta foi criada, porém não foram definidos atributos e instanciados objetos para ela. Ambos são uma característica básica dos programas orientados a objetos.

#Nas linguagens orientadas a objetos, para se instanciar objetos, é preciso criar os construtores da classe. Em Python, a palavra reservada __init__() serve para a inicialização de classes, como é possível verificar a seguir:


class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo): #Método construtor
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo


#Diferentemente de outras linguagens de programação orientadas a objetos, o Pyhton constrói os objetos em duas etapas. A primeira etapa é utilizada com a palavra reservada __new__, a qual, em seguida, executa o método __init__.
#O __new__ cria a instância e é utilizado para alterar as classes dinamicamente nos casos de sistemas que envolvam metaclasses e frameworks. Após __new__ ser executado, esse método chama o __init__ para a inicialização da classe como seus valores iniciais

#Analisando o exemplo, vimos a utilização da palavra self como parâmetro no construtor. Como o objeto já foi instanciado implicitamente pelo __new__, o método __init__ recebe uma referência do objeto instanciado como self.
#Analisando o restante do construtor da figura Classe Conta, notamos que o código possui diversos comandos self, o que indica uma referência ao próprio objeto.
#Por exemplo, o comando self.numero é uma indicação de que o número é um atributo do objeto, ao qual, por sua vez, é atribuído um valor.
#O restante dos comandos self indica a criação dos atributos cpf, nomeTitular e saldo referentes à classe Conta.


#Agora, vamos instanciar o nosso objeto com o método __init__ 

def main():
    c1 = Conta(1,1,"Joao",1000) # Objeto sendo instanciado
    print (f"Nome do titular da conta: {c1.nomeTitular}")
    print (f"Número da conta: {c1.numero}")
    print (f"CPF do titular da conta: {c1.cpf}")
    print (f"Saldo da conta: {c1.saldo}")

# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script

if __name__ == "__main__":
    main()

