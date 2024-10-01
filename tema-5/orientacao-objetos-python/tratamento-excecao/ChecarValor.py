from ExcecaoCustomizada import ExcecaoCustomizada

def checa_valor(valor):
    if valor < 0:
        raise ExcecaoCustomizada("Valor não pode ser negativo!")


#Neste exemplo, ao detectar um valor negativo, a função checa_valor interrompe sua execução normal e lança a exceção ExcecaoCustomizada, transmitindo uma mensagem explicativa.
#Esse mecanismo é essencial para garantir que condições indesejadas sejam tratadas adequadamente.

##################

#Uma vez que uma exceção tenha sido lançada, é importante saber como tratá-la.
#O bloco try...except é a ferramenta adequada para esse propósito:

try:
    checa_valor(-10)
except ExcecaoCustomizada as ex:
    print(f"Exceção lançada: {ex}") 

#Neste código, a função checa_valor é chamada com um valor negativo, o que resulta na exceção ExcecaoCustomizada sendo lançada. 
#O bloco try...except captura essa exceção, e o programa trata o erro de forma controlada, exibindo a mensagem associada à exceção.

