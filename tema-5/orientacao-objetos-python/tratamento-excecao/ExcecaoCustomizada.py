#Python também permite a criação de exceções personalizadas, que são úteis quando se deseja capturar e tratar erros específicos de um determinado contexto da aplicação. 
#Para criar uma exceção personalizada, utilizamos a herança da classe Exception, conforme o exemplo a seguir:

class ExcecaoCustomizada(Exception):
    pass

#A classe ExcecaoCustomizada define uma nova exceção que pode ser lançada e tratada separadamente das exceções padrão de Python.
#O uso do comando pass indica que não há necessidade de adicionar comportamento específico à exceção; a distinção pelo nome é o suficiente.

