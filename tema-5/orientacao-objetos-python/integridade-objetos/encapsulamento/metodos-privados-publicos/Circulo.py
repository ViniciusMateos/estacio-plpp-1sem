#As mesmas regras definidas para atributos são válidas para os métodos das classes. Desse modo, o método pode ser declarado como privado, mesmo que ainda possa ser chamado diretamente como se fosse um método público.
#Os dois underscores antes do método indicam que ele é privado.

class Circulo:

  def __init__(self,clientes,numero,saldo):
    self.clientes = clientes
    self.numero = numero
    self.saldo = saldo
      
  def __gerarsaldo(self):
    print(f"numero: {self.numero}\n saldo:{self.saldo}")

#No código, foi definido o método __gerarsaldo como privado. Portanto, ele pode ser acessado apenas internamente pela classe Conta.
#Um dos principais padrões da orientação a objetos consiste nos métodos públicos e nos atributos privados. Desse modo, respeita-se o encapsulamento.

