# Funcoes
def soma(a,b):
    return a+b

# print(soma(1,2))
# Classe
class Calculadora:
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
    def subtracao(self):
        return self.a-self.b
    def multiplicacao(self):
        return self.a*self.b
calculadora = Calculadora(10,2)
print(calculadora.subtracao())
print(calculadora.multiplicacao())


