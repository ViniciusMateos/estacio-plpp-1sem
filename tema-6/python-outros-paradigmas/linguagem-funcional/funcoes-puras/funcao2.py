
valor = 20

def multiplica(valor, fator):
    valor = valor * fator
    return valor

def main():
    numero = int(input())
    print("Resultado", multiplica(valor, numero))
    print("Resultado", multiplica(valor, numero))

if __name__ == "__main__":
    main()

# Utilizamos a variável valor e a função numero como parâmetros para a função multiplica. O valor da variável numero será recebido via teclado, por meio da função nativa input. 
# As duas vezes em que executamos essa função (linhas 10 e 11), retornarão o mesmo valor. 
# Por exemplo, se o valor de numero for 3, ambas as saídas do script serão: “Resultado 60
# A função multiplica deste script é um exemplo de função pura, pois depende apenas de seus parâmetros para gerar o resultado, e não acessa ou modifica nenhuma variável externa à função e retorna um valor.
