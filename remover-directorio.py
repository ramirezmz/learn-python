import os

try:
    os.rmdir('./testando-criacao')
    print('Pasta removida com sucesso')
except PermissionError as erro:
    print('Sem permissoes para criar pasta')
    print('Descricao: ', erro)
