# Subclasse Gato que sobrescreve os métodos falar e mover

from Animal import Animal

class Gato(Animal):
    def falar(self):
        return "Miau!"

    def mover(self):
        return f"{self.nome} está andando."