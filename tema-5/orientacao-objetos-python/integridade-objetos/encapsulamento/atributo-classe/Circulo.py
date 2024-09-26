#Existem algumas situações em que os sistemas precisam controlar valores associados à classe, e não aos objetos (instâncias) das classes.
#É o caso, por exemplo, ao se desenvolver um aplicativo de desenho, como o Paint, que precisa contar o número de círculos criados na tela.

class Circulo():
  def __init__(self, pontox, pontoy, raio):
    self.pontox = pontox
    self.pontoy = pontoy
    self.raio = raio

#No entanto, conforme mencionamos, é necessário controlar a quantidade de círculos criados.

class Circulo():
  
    total_circulos = 0 #atributo dentro da classe e não do construtor.

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio

#Na linha 14, indicamos para o interpretador que seja criada uma variável total_circulos. Como a declaração está localizada antes do init, o interpretador “entende” que se trata de uma variável de classe, ou seja, que terá um valor único para todos objetos da classe.

#o programa abaixo que irá criar dois círculos. 

class Circulo():

    total_circulos = 0  # Atributo de classe

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        Circulo.total_circulos += 1  # Incrementando o atributo de classe

circ1 = Circulo(1, 1, 10)
print(circ1.total_circulos)  # Isso agora imprimirá 1

circ2 = Circulo(2, 2, 20)
print(circ1.total_circulos)  # Isso agora imprimirá 2
print(circ2.total_circulos)  # Isso também imprimirá 2

print(Circulo.total_circulos)  # Isso imprimirá 2, já que é o valor compartilhado por todas as instâncias

#Cada vez que uma nova instância de Circulo é criada, o método __init__ é chamado. Dentro deste método, Circulo.total_circulos += 1 é utilizado para incrementar o valor de total_circulos diretamente na classe Circulo.
#Quando acessamos circ1.total_circulos ou circ2.total_circulos, estamos na verdade acessando o valor de Circulo.total_circulos, porque total_circulos é um atributo de classe, e todas as instâncias compartilham o mesmo valor.
#Isso significa que, independentemente de qual instância é usada para acessar o atributo, o valor será o mesmo, representando o total acumulado de instâncias criadas.

#No final do programa, ao acessar Circulo.total_circulos diretamente, o valor mostrado também será 2, confirmando que o atributo de classe é compartilhado e reflete o número total de instâncias criadas até o momento.
#O uso de total_circulos como um atributo de classe permite que o programa mantenha um registro centralizado e atualizado do número de objetos Circulo em qualquer ponto da execução.

#No entanto, o acesso direto ao valor da variável de classe não é ideal em boas práticas de programação. Para seguir as convenções de encapsulamento, a variável de classe deveria ser marcada como privada, usando um underscore (_) antes do seu nome, tornando-se _total_circulos.
#Isso protege o atributo de acessos não intencionais ou modificações diretas, encorajando o uso de métodos controlados para acessar ou modificar seu valor

#Como isso fica agora? 


class Circulo():

    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        Circulo._total_circulos += 1

circ1 = Circulo(1, 1, 10)
print(circ1._total_circulos)

circ2 = Circulo(2, 2, 20)
print(circ2._total_circulos)

print(Circulo.total_circulos)
#O comando print(Circulo.total_circulos) tenta acessar diretamente o atributo total_circulos da classe Circulo.
#No entanto, como o atributo foi definido como _total_circulos (com underscore), tornou um atributo privado e não visível fora da classe.
#Isso resultará em um erro de atributo (AttributeError), pois o Python não encontrará Circulo.total_circulos.