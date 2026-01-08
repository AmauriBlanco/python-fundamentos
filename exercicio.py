# 1 Escreva um programa que le dois nomes e retorna uma string formatada no formato "UltimoNOme, PrimeiroNome"
# 2 Inverta a ordem das palavras em uma string fornecida
# 3 Verifique se uma string é um palíndromo

# primeiroNome = input("Digite o primeiro nome: ")
# ultimoNome = input("Digite o último nome: ")

# print(f"{ultimoNome}, {primeiroNome}")
# print(f"{ultimoNome[::-1]}, {primeiroNome[::-1]}")
# print(f"o nome {primeiroNome} é igual a {primeiroNome[::-1]}? = {primeiroNome == primeiroNome[::-1]}")
# print(f"o nome {ultimoNome} é igual a {ultimoNome[::-1]}? = {ultimoNome == ultimoNome[::-1]}")

produtos = {}
novoProduto = (input())
novoValor = (float(input()))

produtos[novoProduto] = novoValor

novoProduto = (input())
novoValor = (float(input()))

produtos[novoProduto] = novoValor

novoProduto = (input())
novoValor = (float(input()))

produtos[novoProduto] = novoValor

print(produtos)
produtoMaisCaro = max(produtos, key=produtos.get)
print(produtoMaisCaro)
media = sum(produtos.values()) / len(produtos)
print(f"{media:.2}")

