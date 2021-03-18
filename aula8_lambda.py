#funções anônimas são chamadas de lambda, o módulo em python são os arquivos gerados pelo programa
#o comando 'lambda' só é eficiente para funções que podem ser feitas somente em uma linha

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
contador_letras(lista_animais)
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5,10))
print(subtracao(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, : a / b,
}
#acima tem um exemplo de dicionário, ou seja várias funções dentro de uma variável. Usa-se as { } para evidenciar as funções

print(type(calculadora))
soma = calculadora['soma']
#a expressão acima representa 'soma': lambda a, b: a + b,
multiplicacao = calculadora['multiplicacao']
print('a soma é: {}'.format(soma(10, 5)))
print('a multiplicação é: {}'.format(multiplicacao(10, 2)))