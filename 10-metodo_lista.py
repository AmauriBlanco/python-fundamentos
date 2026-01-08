filmeMatrix = ["Matrix", 1999, 9.5, True]
listaFilmes = ["Matrix", "Teste2", "Teste3", "Interestelar"]
print(len(filmeMatrix))
print(filmeMatrix.index("Matrix"))

filmeMatrix.append("Senhor dos aneis")

print(filmeMatrix)

listaFilmes.sort()
print(listaFilmes)

filmesCopy = listaFilmes.copy()
filmesCopy.remove("Matrix")
print(filmesCopy)

filmesCopy.clear()
print(filmesCopy)

num1 = int(input())
num2 = int(input())
num3 = int(input())

listaNumeros = []
listaNumeros.append(num1)
listaNumeros.append(num2)
listaNumeros.append(num3)

somaList1 = int(listaNumeros[0])
somaList2 = int(listaNumeros[1])
somaList3 = int(listaNumeros[2])
print(type(somaList))

print(listaNumeros)
print(listaNumeros[0])
