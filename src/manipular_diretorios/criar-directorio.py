import os

try:
    os.mkdir('./testando-criacao')
    print('Pasta criada com sucesso')
except PermissionError as erro:
    print('Sem permissoes para criar pasta')
    print('Descricao: ', erro)
