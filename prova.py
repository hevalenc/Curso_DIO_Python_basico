try:
    lista = [1, 2]
    print(lista[2])
except Exception:
    print('ocorreu um erro desconhecido')
except IndexError:
    print('não foi possível acessar o index pois ele não existe na lista')