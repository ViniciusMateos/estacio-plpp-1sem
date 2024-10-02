# script funcao_iterable.py
lista = [1, 2, 3, 4, 5]

def triplica_itens(iterable):
    lista_aux = []
    for item in iterable:
        lista_aux.append(item*3)
    return lista_aux

def main():
    nova_lista = triplica_itens(lista)
    print(nova_lista)

if __name__ == "__main__":
    main()

#Definimos uma função chamada triplica_itens, que recebe um iterável como parâmetro (linha 4), cria uma lista auxiliar para garantir imutabilidade (linha 5), percorre os itens do iterável passado como parâmetro (linha 6), adiciona os itens triplicados à lista auxiliar (linha 7) e retorna a lista auxiliar (linha 8).
#Essa função é chamada com o argumento lista (linha 11) e o resultado é impresso (linha 12).