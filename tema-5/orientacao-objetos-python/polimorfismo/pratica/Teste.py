from Pato import Pato
from Vaca import Vaca
from Cachorro import Cachorro
from Gato import Gato

# Função que usa polimorfismo para chamar o método falar
def fazer_som(animal):
    return animal.falar()

# Função que usa polimorfismo para chamar o método mover
def fazer_movimento(animal):
    return animal.mover()



cachorro = Cachorro('Lug')
gato = Gato( 'Floquinho')
vaca = Vaca('Mimosa')
pato = Pato("Pato Donald")

# Chamando os métodos polimórficos
print(fazer_som(cachorro))  # Saída: Au!
print(fazer_som(gato))      # Saída: Miau!
print(fazer_som(vaca))      # Saída: Muu!
print(fazer_som(pato))      # Saída: Quack!

print(fazer_movimento(cachorro))  # Saída: O cachorro está andando.
print(fazer_movimento(gato))      # Saída: O gato está andando.
print(fazer_movimento(vaca))      # Saída: A vaca está andando.
print(fazer_movimento(pato))      # Saída: Pato Donald está andando, Pato Donald está nadando E Pato Donald está voando.