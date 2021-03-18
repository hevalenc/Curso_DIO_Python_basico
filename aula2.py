#o símbolo '#' na linha de comando significa cometário

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
#o comando 'int' significa que a entrada é um valor (número) inteiro
#o comando 'input' solicia inserção de dados, ou seja, interação

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
print(type(soma))
#o comando 'type' vai mostrar o tipo da variável, se o valor é 'int' é para inteiro e 'float' é para decimal

print("soma : " + str(soma))
#exemplo de exibição de texto com valor, o comando string converte o número em texto e permitirá a concatenação entre texto e número

print('soma : {}'.format(soma))
#este comando acima éoutra forma de concatenar texto com número, usa-se as chaves e o .format (concatena inteiros e decimais)

print(subtracao)
print(multiplicacao)
print(divisao)
print('soma: {} subtração: {}'. format(soma, subtracao))
#outra forma de exibição de vários valores, o comando "\n" mostra a informação em várias linhas

print('soma: {} \nsubtração: {}'. format(soma, subtracao))