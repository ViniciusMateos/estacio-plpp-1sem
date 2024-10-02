# script funcao_filtro_iterable.py
lista = [1, 2, 3, 4, 5]

def impares(iterable):
    lista_aux = []
    for item in iterable:
        if item % 2 != 0:
            lista_aux.append(item)
    return lista_aux

def main():
    nova_lista = impares(lista)
    print(nova_lista)

if __name__ == "__main__":
    main()

#Definimos uma função chamada ímpares, que recebe um iterável como parâmetro (linha 4), cria uma lista auxiliar para garantir imutabilidade (linha 5), percorre os itens do iterável passados como parâmetros (linha 6), adiciona os itens ímpares à lista auxiliar (linhas 7 e 8) e retorna a lista auxiliar (linha 9).
#Essa função é chamada com o argumento lista (linha 12) e o resultado é impresso (linha 13).

