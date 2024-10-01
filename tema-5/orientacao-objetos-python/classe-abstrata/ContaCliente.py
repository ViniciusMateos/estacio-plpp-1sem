#Toda classe abstrata é uma subclasse da classe ABC (Caelum, 2020). Para tornar a classe Conta Cliente abstrata, muda-se sua definição. 

from abc import ABC, abstractmethod
class ContaCliente(ABC):
    pass

#Para uma classe ser considerada abstrata, ela precisa ter pelo menos um método abstrato. 
#Esse método pode ter implementação, embora isso não faça sentido, pois ele deverá obrigatoriamente ser implementado pelas subclasses.
#Em nosso exemplo, como não teremos o ContaCliente, tal conta não terá Calculo do rendimento.

class ContaCliente(ABC):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento

    @abstractmethod
    def calculo_rendimento(self):
        pass

#Quando se tentar instanciar um objeto da classe, será obtido um erro indicando que essa classe não pode ser instanciada.-

#Ao tentar criar uma instância de ContaCliente com cc1 = ContaCliente(1, 0.1, 0.25, 1000, 0.1), o Python irá lançar um erro do tipo TypeError.
#Esse erro ocorre porque ContaCliente é uma classe abstrata e possui métodos abstratos que não foram implementados.

#Para que o código funcione, você deve criar uma subclasse concreta de ContaCliente que implemente o método calculo_rendimento. Somente depois disso, você poderá instanciar essa subclasse.

#Considerando a modelagem que estamos utilizando, apenas as subclasses ContaComum e ContaVIP podem ser instanciadas.

#As classes mencionadas devem obrigatoriamente implementar os métodos.
#Caso contrário, elas serão classes abstratas e delegarão para as suas subclasses a implementação concreta do método abstrato.
