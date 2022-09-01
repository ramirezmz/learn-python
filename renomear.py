import os

try:
    os.rename('./remover-renomear.py', './remover.py')
    print('Arquivo renomeado')
except FileNotFoundError as erro:
    print(' Arquivo inexistente')
    print('Descricao: ', erro)
except PermissionError as erro:
    print('Sem permissao para acessar o Arquivo')
    print('Descricao: ', erro)
except FileExistsError as erro:
    print('Arquivo destino já existente')
    print('Descricao: ', erro)

print('Termino do programa')
