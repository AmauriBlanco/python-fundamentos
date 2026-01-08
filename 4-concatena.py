name = input("Digite o nome do filme: \n")
yearLaunch = int(input("Digite o ano de lançamento: \n"))
noteMovie = float(input("Digite a nota d filme \n"))

#alternativa 1
print("Dados do Filme")
print("====================")
print("Nome do filme: ", name)
print("Ano de lançamento: ", yearLaunch)
print("Nota do filme: ", noteMovie)

#alternativa 2
print("Dados do Filme")
print("====================")
print("Nome do filme: ", name, "\nAno de lançamento: ", yearLaunch, "\nNota do filme: ", noteMovie)

#alternativa 3
print("Dados do Filme")
print("====================")
print(f"Nome do filme: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota do filme: {noteMovie}")
