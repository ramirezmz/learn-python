#arquivo = open("dados.txt", "r")

#conteudo = arquivo.read()

#print("Tipo do conteúdo: ", type(conteudo))
#print("Conteudo retornado pelo read:")
# print(repr(conteudo))

# arquivo.close()

with open("dados.txt", "r") as arquivo:
    print("Representação da linha após strip")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
