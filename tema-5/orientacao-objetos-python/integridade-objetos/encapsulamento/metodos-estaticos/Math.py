#São métodos que podem ser chamados sem haver uma referência para um objeto da classe, ou seja, não existe a obrigatoriedade da instanciação de um objeto da classe.
#O método pode ser chamado diretamente. 

import math
class Math:

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)
    
#Aqui, o método sqrt da classe Math foi chamado sem que um objeto da classe Math fosse instanciado.

#Os métodos estáticos não são uma boa prática na programação orientada a objetos. Eles devem ser utilizados apenas em casos especiais, como o de classes de log em sistemas.