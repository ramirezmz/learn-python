import os

try:
    entradas = os.scandir('./manipulacao-de-arquivos')

    for obj in entradas:
        print(obj)
        print('Nome: ', obj.name)
        print('Caminho: ', obj.path)
        print('É diretorio: ', obj.is_dir())
        print(' É arquivos: ', obj.is_file())
        if obj.is_file():
            print('Tamanho: ', obj.stat().st_size, 'B')
        print('================================')

except FileNotFoundError:
    print('O caminho nao existe')
except NotADirectoryError:
    print('O caminho nao é de um diretorio')
