#Os métodos de classe são a maneira indicada para se acessar os atributos de classe. Eles têm acesso diretamente à área de memória que contém os atributos de classe.

#Para definir um método como estático, deve-se usar o decorator @classmethod. Observe agora a classe Círculo alterada.

class Circulo():

    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos +=1


    @classmethod
    def get_total_circulos(cls):
        return cls._total_circulos

circ1 = Circulo(1, 1, 10)
circ2 = Circulo(2, 2, 20)

print(Circulo.get_total_circulos())

#No código, o método type(self)._total_circulos += 1 é utilizado para incrementar _total_circulos a cada vez que uma nova instância é criada.
#Usar type(self)._total_circulos é equivalente a usar Circulo._total_circulos, mas permite que o código funcione corretamente mesmo se for usado em subclasses, garantindo que o incremento seja realizado na classe apropriada.

#O método get_total_circulos é marcado com o decorador @classmethod, o que significa que ele pode ser chamado diretamente na classe Circulo ou em qualquer uma de suas instâncias.
#Esse método retorna o valor atual do atributo _total_circulos, permitindo acessar quantas instâncias de Circulo foram criadas.

#No exemplo de uso, duas instâncias de Circulo (circ1 e circ2) são criadas, cada uma chamando o método __init__, que incrementa _total_circulos.

# Após a criação de circ1, _total_circulos é 1.
# Após a criação de circ2, _total_circulos é 2.
# O método Circulo.get_total_circulos() retorna 2, que é o número total de instâncias criadas até o momento.
