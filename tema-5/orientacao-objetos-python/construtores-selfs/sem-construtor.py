#É importante ressaltar que, em Python, não é obrigatório ter um método construtor na classe. Isso ocorrerá apenas se for necessária alguma ação na construção do objeto, como a inicialização e/ou a atribuição de valores

#A seguir um exemplo de uma classe sem um método construtor.

class A():
    def f(self):
        print("foo")


def main():
    obj_A = A() # Objeto sendo instanciado
    obj_A.f()

if __name__ == "__main__": 
    main()