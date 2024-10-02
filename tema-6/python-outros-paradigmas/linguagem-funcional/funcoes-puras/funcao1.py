valor = 20

def multiplica(fator):
    global valor
    valor = valor * fator
    print("Resultado", valor)

def main():
    numero = int(input())
    multiplica(numero)
    multiplica(numero)
 
# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual à "__main__".
# Nesse caso, a condição do IF a seguir será TRUE,
# então o que está no corpo do IF será executado. 
# No caso, é um chamado ao método main do script
 
if __name__ == "__main__":
    main()


# Definimos uma função chamada multiplica, que multiplica a variável global valor por um fator passado como parâmetro. 
# O valor do resultado é atribuído à variável valor novamente (linha 6), que é impresso em seguida (linha 7).
# Por exemplo, se chamarmos a função multiplica pela primeira vez, passando o valor 3  como parâmetro, obteremos a saída “Resultado 60”. 
# Como modificamos a própria variável global valor no corpo da função, ao chamarmos novamente a função multiplica passando novamente o 3 como parâmetro, obtemos um resultado de saída diferente: “Resultado 180”.
# Além de não depender apenas dos parâmetros, essa função não retorna valor algum. A função multiplica deste script não é pura.
