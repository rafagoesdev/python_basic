# div = 0
# x= 0
# a=0
# for x in range(101):
#     for a in range(1, x+1):
#         resto = x % a
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print('Número {} é primo'.format(x))
#     div = 0
nota = int(input("Entre com uma nota: "))
while nota>10:
    nota = int(input("Entre com uma nota de 0 a 10: "))
nota1 = int(input("Entre com uma nota: "))
while nota1>10:
    nota1 = int(input("Entre com uma nota de 0 a 10: "))
nota2 = int(input("Entre com uma nota: "))
while nota2>10:
    nota2 = int(input("Entre com uma nota de 0 a 10: "))
media=(nota1+nota2+nota)/3
print("média: {}".format(media))

