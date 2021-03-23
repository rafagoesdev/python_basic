from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data = date.today()
    print(data.strftime('%d/%m/%Y'))
    # strftime - formatar conforme documentação Python
    data_str = data.strftime('%A %B %C')
    # data em sting
    print(data_str)

def trabalhando_com_time():
    hora = time(hour=15, minute=30, second=20)
    print(hora)
    print(hora.strftime('%H:%M:%S'))

def trabalhando_com_datetime():
    data = datetime.now()
    print(data)
    print(data.strftime("%d/%m/%Y, %H:%M"))
    print(data.strftime('%c'))
    print(data.day)
    print(data.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data.weekday()])
    data_criada = datetime(2018,6,20,15,32,32)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2020'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida.date())
    novadata = data_convertida - timedelta(days=365, hours=5, minutes=12,seconds=30)
    print(novadata)

if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()