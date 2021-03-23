def conta_letras(lista):
    contador = []
    for x in lista:
        quant = len(x)
        contador.append(quant)
    return contador

if __name__ == '__main__':
    lista = ['nezes', 'cat']
    print(conta_letras(lista))