
conjunto = {1,2,3,4,4,4,4}
conj2 = {4,7,8,9}
print(type(conjunto))
print(conjunto)
conjunto.add(5)
conjunto.discard(2)

uniao=conj2.union(conjunto)
print(uniao)

interseccao=conjunto.intersection(conj2)
print(interseccao)

diferenca1 = conjunto.difference(conj2)
dif2 = conj2.difference(conjunto)
print(diferenca1)
print(dif2)

difsimetrica = conjunto.symmetric_difference(conj2)
print(difsimetrica)

# conj_a = {1,2,3}
# conj_b = {1,2,3,4,5}
# conj_subset = conj_b.issubset(conj_a)
# print(conj_subset)
# # subset - quando um é subconjunto de outro

# conj_superset = conj_b.issuperset(conj_a)
# print(conj_superset)
# # superset - inverso de subset
#
# lista = [1,2,2,3]
# print(lista)
# conj_lista = set(lista)
# print(conj_lista)
# lista = list(conj_lista)
# print(lista)