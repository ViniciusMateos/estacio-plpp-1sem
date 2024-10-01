from Divisao import divide
from ChecarValor import checa_valor
from ExcecaoCustomizada import ExcecaoCustomizada


try:
    resultado = divide(10, 0)
except ZeroDivisionError as ex:
    print(f"Erro de divisão por zero: {ex}")

try:
    checa_valor(-10)
except ExcecaoCustomizada as ex:
    print(f"Exceção personalizada lançada: {ex}")


#O bloco try...except é utilizado para tentar executar as funções e capturar qualquer exceção que seja lançada. 
#No primeiro bloco, tentamos dividir 10 por 0, o que gera uma ZeroDivisionError. Essa exceção é capturada e uma mensagem de erro é exibida.

#No segundo bloco try...except, chamamos checa_valor(-10), o que resulta na exceção personalizada ExcecaoCustomizada sendo lançada.
#O bloco except captura essa exceção e exibe a mensagem associada.


#O tratamento de exceções é uma prática fundamental na programação em Python, permitindo que os programas sejam mais robustos e resilientes a erros. 
#Esse exemplo destaca a flexibilidade de Python em permitir a criação de exceções personalizadas, que podem ser utilizadas para capturar e tratar condições específicas da lógica do seu programa.
#Isso é especialmente útil em projetos maiores, onde a clareza e a especificidade dos erros são cruciais para a manutenção e depuração do código.

