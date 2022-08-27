import os


arquivo = open("test.txt")

print("Arquivo aberto com sucesso!")
print(os.path.relpath(arquivo.name))
print(arquivo)
