#o comando 'while True' é usado para loop com função verdadeira
#o comando 'break' força a saída do loop quando o comando acima der certo (passar)

class Error(Exception):
    pass
#criado uma classe para permitir customização de erros para exceções

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('entre com uma nota de 0 a 10 : '))
        print(x)
        if x > 10:
            raise InputError('nota não pode ser maior que 10')
        #o comando 'raise' força uma exceção
        elif x < 0:
            raise InputError('nota não pode ser menor que 0')
        break
    except ValueError:
        print('valor inválido, deve-se digitar apenas números')
    except InputError as ex:
        print(ex)

