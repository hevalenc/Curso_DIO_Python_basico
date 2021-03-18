#o comando 'from' pode serusado para chamar um arquivo python e o comando 'import' pode chamar todo o arquivo ou somente
#um módulo ou definição ('def') para este caso usa-se o 'from' antes. Lembrando de usar o comando 'main'(if __name__ == '__main__':)
# no arquivo origem para chamar a classe

from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora= Calculadora(5, 10)
    print(calculadora.soma())
    lista= ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra da lista: {}'.format(total_letras))
    print(teste())
