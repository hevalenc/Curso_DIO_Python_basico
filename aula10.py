#o 'datetime' é uma biblioteca do python, o comando 'strftime' serve para usar a biblioteca de data e hora
#'%d/%m/%y' e '%A %B %Y' são diretivas para definir o formato de exibição de data
#'%H:%M:%S' diretiva para horas,

from datetime import date, time, datetime, timedelta


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.weekday())
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
    print(tupla[data_atual.weekday()])
    #foi usado a tupla para chamar o dia da semana, como no exemplo
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2)
    print(nova_data)
    nova_data1 = data_convertida + timedelta(days=365, hours=2)
    print(nova_data1)


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))
#print(data_atual.strftime('%d/%m/%y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
