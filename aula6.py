#lista recebe colchetes, tupla recebe parenteses, conjuntos recebe chaves
#conjunto não repete os valores caso estejam repetidos e são aritméticos

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
#o comando '.union' é utilizado para unir grupos

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
#o comando '.intersecion' é utilizado para verificar a intersecção entre os grupos (números iguais)

conjunto_diferença = conjunto.difference(conjunto2)
conjunto_diferença2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferença))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferença2))
#o comando '.difference' é utilizado para mostrar a diferença de um conjunto para outro

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))
#o comando '.symmetric_difference' é utilizado para mostrar todos os valores que não são repetidos nos dois gupos

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))
#o comando'.issubset' é utilizado para verificar se um conjunto pertence ao outro, ou seja, sub-conjunto
#este comando vai dar o resultado 'true' para positivo e 'false' para negativo

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))
#o comando '.issuperset' é utilizado para verificar se um conjunto contém o outro conjunto, ou seja, se possui todos os valores do outro
#este comando vai dar o resultado 'true' para positivo e 'false' para negativo

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
#o comando 'set' é usado para converter uma lista em um conjunto e remove as duplicidades da lista quando tiver

lista_animais = list(conjunto_animais)
print(lista_animais)
#o comando 'list'  converte para lista, neste exemplo as repetiçoes da lista original foram removidas´~

# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)
# #o comando '.add' serve para adicionar elementos e o comando '.discard' serve para remover elementos, pode-se utilizar também o comando 'remove'
