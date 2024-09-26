#polimorfismo e herança em Python, criando um sistema de classes que modela diferentes tipos de animais e suas habilidades de movimento e fala. 
#Você vai definir uma classe base, criar subclasses específicas para adicionar capacidades de movimento.

# Classe base para todos os animais
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

    def mover(self):
        pass

    # Função que usa polimorfismo para chamar o método falar


