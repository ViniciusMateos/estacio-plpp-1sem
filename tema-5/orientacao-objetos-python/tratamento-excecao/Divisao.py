#Um exemplo clássico de exceção ocorre ao tentar realizar uma divisão por zero, o que em Python resulta na exceção ZeroDivisionError.
#Para ilustrar o tratamento desse tipo de erro, considere o seguinte exemplo:

#Neste código, ao tentar dividir 10 por 0, Python lança uma exceção ZeroDivisionError. 
#O bloco try...except captura essa exceção, permitindo que o programa lide com o erro de forma controlada, imprimindo uma mensagem de erro personalizada em vez de interromper a execução do programa.



def divide(a, b):
    return a / b

try:
    resultado = divide(10, 0)
except ZeroDivisionError as ex:
    print(f"Erro: {ex}") 