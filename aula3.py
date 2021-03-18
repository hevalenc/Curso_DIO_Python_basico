a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('você digitou errado. \nprimeiro bimestre: '))
b = int(input('segundo bimestre: '))
if b > 10:
    b = int(input('você digitou errado. \nsegundo bimestre: '))
c = int(input('terceiro bimestre: '))
if c > 10:
    c = int(input('você digitou errado. \nterceiro bimestre: '))
d = int(input('quarto bimestre: '))
if d > 10:
    d = int(input('você digitou errado. \nquarto bimestre: '))
media = (a + b+ c + d) / 4
print('média: {}'.format(media))
#lembrando o comando '.format' permite concatenar letras com numeros


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('média: {}'.format(media))
# else:
#     print('foi informado alguma nota errada')
#alternativa para programar a média de 4 notas com validações

# a = int(input('entre com o primeiro valor: '))
# b = int(input('entre com o segundo valor '))
# #'comando 'int' vai converter o número para inteiro
# resto_a = a % 2
# resto_b = b % 2
# #o comando '%' foi utilizado para verificar se o número é divisível por outro
# if resto_a == 0 or not resto_b > 0:
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')
##programação com verificação de número par usando comandos condicionais


# a = input('primeiro valor: ')
# b = input('segundo valor: ')
# c = input('terceiro valor: ')
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# #a tabulacão da linha abaixo do comando 'if' significa que a linha pertence ao comando 'if'
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# #o comando 'elif' significa caso se
# else:
#     print('o maior número é {}'.format(c))
# #o comando 'else' significa senão
#
# print('final do programa')
##programação com ""condição lógica""