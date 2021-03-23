lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    #  divisao = 10/0
    # # print(lista[3])
    # x = a
except ZeroDivisionError:
    print('Divisão por zero impossível')
except ArithmeticError:
    print('Erro em operação aritmética')
except IndexError:
    print('Erro - índice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Nenhuma exceção ocorrida')
finally:
    print('sempre executa')
    arquivo.close()
