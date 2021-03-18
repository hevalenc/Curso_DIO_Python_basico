#o comando 'open' serve para abrir um arquivo existente ou criar um novo arquivo, o comando 'w' é write - escrever
#o comando 'close' fecha o arquivo. O arquivo pode ser gerado em qualquer diretório uma vez que se coloca o endereço
#o comando 'write' escreve uma informação no arquivo, se o arquivo tem algum conteúdo, atenção com a letra na linha 'open'
#o 'w' escreve algo novo e apaga a escrita anterior do arquivo; o 'a' adiciona nova escrita e mantém o antigo
#o 'r' é usado para leitura

import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/Haed e Heitor/PycharmProjects/projeto_python/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #o comando 'split' com o '\n' vai separar as informações pelo enter
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        #o comando 'split' com o ',' vai separar as informações pela vírgula
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        #esta linha é usadoo 'lambda' para simplificar a função e já está rodando a conversão de strings para inteiros
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/Users/Haed e Heitor/PycharmProjects/')
    #se não colocar nome irá ser mantido o nome do arquivo, se colocaar outro nome, será copiado o arquivo com outro nome

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Haed e Heitor/PycharmProjects/')

if __name__ == '__main__':
    # move_arquivo('notas.txt')
    copia_arquivo('notas.txt')
    lista_media = media_notas('notas.txt')
    print(lista_media)
    escrever_arquivo('Primeira linha.\n')
    aluno = 'cesar, 7, 9, 3, 8\n'
    atualizar_arquivo('notas.txt', aluno)
    ler_arquivo('teste.txt')