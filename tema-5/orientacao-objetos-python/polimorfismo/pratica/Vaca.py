# Subclasse Vaca que sobrescreve os métodos falar e mover

from Animal import Animal

class Vaca(Animal):
    def falar(self):
        return "Muu!"

    def mover(self):
        return f"{self.nome} está andando."