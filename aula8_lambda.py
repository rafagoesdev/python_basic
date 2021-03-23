contador = lambda lista: [len(x) for x in lista]

lista1 = ['lkcmls',"kjdnla"]

print(contador(lista1))

# soma = lambda a,b: a+b
#
# print(soma(1,2))

calculadora = {
    'soma': lambda a,b: a+b,
    'sub': lambda a, b: a - b,
    'multi': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
print('A soma é {}'.format(soma(2,4)))