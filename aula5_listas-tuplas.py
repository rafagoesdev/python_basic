lista = [1, 3, 2, 7]
print(lista[1])
print(sum(lista))
print(max(lista))

if 1 in lista:
    print('1 está na lista')

lista.append(411)
print(lista)

# lista.pop(2)
# print(lista)
#
# lista.remove(7)
# print(lista)

lista.sort()
print(lista)

lista.reverse()
print(lista)

# tupla (imutavel)
tupla = (1,21,2,1,2)
print(tupla[1])

print(len(lista))
print(len(tupla))

# converter lista em tupla
tuplanum = tuple(lista)

# converter tupla em lista
listanum = list(tupla)
print(listanum)