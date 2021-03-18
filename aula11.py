#tratamento de erros e exceções com o comando 'try' e 'except'
#a definição 'ZeroDivisionError' éum módulo pertencente a biblioteca python para tratamento específico

lista= [1, 10]
arquivo = open('teste.txt', 'r')
try:
    divisao = 10 /1
    numero = lista[1]
    # x = a
    # divisao = 10 / 0
#erro forçado para verificação do tratamento de erro com o comando 'except'

except ZeroDivisionError:
    print('não é possível realizar uma divisão por zero')
except ArithmeticError:
    print('não é possível realizr uma operação aritmética')
except IndexError:
    print('erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
#'BaseException' é a base de dados topo de todas as exceções, o 'Exception' é uma derivação do 'BaseException'
#'ZeroDivisionError' é uma derivação do 'ArithmeticError'
# except:
#     print('erro desconhecido')
##tratamento de erro de forma generica

else:
    print('executa quando não ocorre erro')

finally:
    print('sempre executa')
    print('fechando arquivo')
    arquivo.close()
#o comando 'finally' executa os comandos sem considerar os módulos anteriores, neste caso o bloco de tratamento de erros
