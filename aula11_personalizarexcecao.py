class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
while True:
    try:
        x = int(input('Entre com nota de 0 a 10 '))
        print(x)
        if x > 10:
            raise InputError('Nota deve ser menor que 10')
        elif x < 0:
            raise InputError('Nota deve ser maior que zero')
        break
    except ValueError:
        print('Valor inválido ')
    except InputError as ex:
        print(ex)