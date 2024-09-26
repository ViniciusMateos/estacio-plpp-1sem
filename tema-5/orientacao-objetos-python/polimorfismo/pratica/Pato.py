# Subclasse Pato que herda de Animal, Voador e Nadador

from Animal import Animal
from Nadador import Nadador
from Voador import Voador

class Pato(Animal, Voador, Nadador):

      def falar(self):
        return "Quack!"

      def mover(self):
        return f"{self.andar()}, {self.nadar()} E {self.voar()}"

      def andar(self):
        return f"{self.nome} está andando."