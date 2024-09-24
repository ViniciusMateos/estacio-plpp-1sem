#Crie uma classe chamada televisão que siga os requisitos a seguir:
    #Receba como parâmetros em seu construtor o canal inicial, o maior canal e o menor canal.
    #Possua como atributos o canal sintonizado, o número do maior canal e o número do menor canal.
    #Possua dois métodos, um para diminuir o canal atual e outro para aumentar o canal sintonizado.
    #Instancie uma tv e teste as trocas de canal.



class Televisao:
    def __init__(self, pcanal, min, max): #Método construtor
        self.canal = pcanal
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin: #Processo para que ele não ande mais canais para baixorocesso para que ele não ande mais canais para cima do limite estipulado do limite estipulado
            self.canal -= 1
        else:
            self.canal = self.cmax


    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax: #Processo para que ele não ande mais canais para cima do limite estipulado
            self.canal += 1
        else:
            self.canal = self.cmin

print('TV1\n')

tv1 = Televisao(2 , 2,  10 )
print(f"Canal Sintonizado: ",tv1.canal)

for x in  range (1,20): #Passando para mudar o canal para cima 20 vezes
    tv1.muda_canal_para_cima()
    print(f"Canal Sintonizado: ",tv1.canal)

print('\nTV2\n')

tv2 = Televisao(10, 2, 10)
print(f"Canal Sintonizado: ",tv2.canal)
print(f"Mudando canal para baixo")
for x in  range (1,20): #Passando para mudar o canal para baixo 20 vezes
    tv2.muda_canal_para_baixo()
    print(f"Canal Sintonizado: ",tv2.canal)