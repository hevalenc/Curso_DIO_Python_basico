#a lista é mutável e a tupla não, a lista usa colchetes e a tupla usa parenteses

lista = [1, 9, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
#o comando 'lista' é acompanhado pelo simbolo colchete e o contador sempre inicia pelo 0 (primeiro item da lista)

lista_animal[0] = 'macaco'
print(lista_animal)
#este comando faz a substituição do valor de uma lista, conforme a posição indicada

tupla = (1, 10, 12, 14)
print(len(tupla))
# o comando 'len' fará a contagem de quantos valores tem na lista

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
#o comando 'tuple' é utilizado para converter uma lista em tupla

lista_numéria =list(tupla)
print(type(lista_numéria))
print(lista_numéria)
#o comando 'list' é utilizado para converter uma tupla em lista


# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# #o comando '.sort' é utilizado para ordenar os valores da lista em ordem crescente
#
# lista_animal.reverse()
# print(lista_animal)
# #o comando '.reverse' éutilizado para ordenar os valores da lista de trás para frente

# nova_lista = lista_animal * 3
# print(nova_lista)
# #pode-se multiplicar os itens da lista com este comando acima, os itens serão repetidos pelo número de vezes citado

# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista, será incluído')
#     lista_animal.append('lobo')
#     print(lista_animal)
# #usando um comando condicional para verificar se o valor está na lista
# #o comando '.append' adiciona valores na lista

# lista_animal.remove('elefante')
# print(lista_animal)
# #o comando '.remove' é utilizado para remover um valor da lista

# lista_animal.pop(0)
# print(lista_animal)
# #o comando '.pop' é utilizado para retirar um valor da lista, se o parenteses ficar vazio será removido o último valor

# print(lista_animal[1])
# #o número entre colchetes indica qual será o valor mostrado na tela, a sequência da lista começa com zero

# print(min(lista))
# #o comando 'min' pode ser utilizadopra mostrar o menor valor que está na lista
# #se utilizado o comando 'min' com uma lista com strings(nomes) será mostrado o string com a menor letra inicial conforme o alfabeto

# print(max(lista))
# #o comando 'max' pode ser utilizado para mostrar o maior valor que está na lista
# #se utilizado o comando 'max' com uma lista com strings(nomes) será mostrado o string com a maior letra inicial conforme o alfabeto

# print(sum(lista))
# #o comando 'sum' irá somar todos os valores da lista como neste exemplo

# for x in lista:
#     print(x)
# #o comando 'for' e 'in' criam um laço e, neste caso, irá rodar todos os elementos da lista