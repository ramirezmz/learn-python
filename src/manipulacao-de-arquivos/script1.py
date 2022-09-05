arquivo = open("./test.txt", "r")

conteudo = arquivo.read()

print("Tipo do conteúdo: ", type(conteudo))

print("Cnteúdo retornado pelo read:")
print(repr(conteudo))

arquivo.close()
