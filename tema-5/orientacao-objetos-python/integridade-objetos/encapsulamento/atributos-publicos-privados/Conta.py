# Para seguir o encapsulamento e proibir alterações indevidas dos atributos, deve-se definir atributos privados para a classe.
# Por default, em Python, os atributos são definidos como público, ou seja, podem ser acessados diretamente sem respeitar o encapsulamento – acesso feito apenas por meio de métodos do objeto.

# Para tornar um atributo privado, é preciso iniciá-lo com dois underscores (‘__’). 
# E qual seria o retorno do interpretador ao se acessar um atributo privado para classe Conta? Um erro seria gerado.

class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero #atributoprivado
        self.__saldo = saldo #atributoprivado

def main():
        conta = Conta(1, 1000)
        saldo = conta.saldo

if __name__ == "__main__":
    main()

#O erro gerado indica que não existe o atributo saldo. Mas como não existe se ele está na definição da classe? Ele realmente existe, mas não está visível para o programa porque o atributo é privado.
#É importante ressaltar que, em Python, não há realmente atributos privados. O interpretador renomeia o atributo privado para _nomedaClasse__nomedoatributo.
#O atributo, portanto, ainda pode ser acessado. Embora ele funcione, isso é considerado uma prática que viola o princípio de encapsulamento da orientação a objetos.

def main():
        conta = Conta(1, 1000)
        print(conta._Conta__saldo)

if __name__ == "__main__": # executando aqui, ele retornará o valor "privado" que na verdade foi apenas renomeado.
    main()