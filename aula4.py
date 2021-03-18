a = int(input('primeiro bimestre: '))
while a > 10:
    a = int(input('você digitou errado. \nprimeiro bimestre: '))
b = int(input('segundo bimestre: '))
while b > 10:
    b = int(input('você digitou errado. \nsegundo bimestre: '))
c = int(input('terceiro bimestre: '))
while c > 10:
    c = int(input('você digitou errado. \nterceiro bimestre: '))
d = int(input('quarto bimestre: '))
while d > 10:
    d = int(input('você digitou errado. \nquarto bimestre: '))
media = (a + b+ c + d) / 4
print('média: {}'.format(media))
#o comando 'while' cria um loop infinito até que o valor correto seja inserido

# nota = int(input('entre com a nota: '))
# while nota > 10:
#     nota = int(input('nota inválida. \nentre com a nota correta: '))
#exemplo 2

# a = 0
# while a <= 10:
#     print(a)
#     a += 1
#exemplo de laço 'while' que substitui o 'for' com 'range'

#programação com o laço 'for' e 'range'
# # a = int(input('entre com o número: '))
# #este comando acima foi substituído pelo comando 'for' e 'range'
#
# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
# #ou pederá usar div = div + 1
#     if div == 2:
#         print(num)
#         #só serão impressos números primos
#
#     # if div == 2:
#     #     print('número {} é primo'.format(num))
#     # else:
#     #     print('número {} não é primo'.format(num))
#     #estas linhas de comando acima foram usados em um exemplo
# #o comando '%' é um mode
# #esta progrmação vai verificar os número primos (são números divisiveis por 1 e por ele mesmo)