# script funcao_map_lambda.py
lista = [1, 2, 3, 4, 5]

nova_lista = map(lambda item: item * 3, lista)# função lambda

def main():
    print(list(nova_lista))

if __name__ == "__main__":
    main()

#Substituímos a função triplica pela função lambda (lambda item: item*3), que foi utilizada como argumento para a função map (linha 4). 
#Esta vai aplicar a função lambda em cada item da lista, retornando um novo iterável que foi impresso posteriormente (linha 7).

#Observe como o código foi reduzido e mesmo assim preservamos a utilização de funções puras (lambda), alta ordem (map) e que preservaram a imutabilidade dos dados.
#Tudo isso para garantir que não haja efeitos colaterais e dependência de estados.

