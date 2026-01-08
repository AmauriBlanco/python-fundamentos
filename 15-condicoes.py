# name = input("Digite o nome do Filme:\n")
# yearRelease = int(input("Digite o ano de lançamento:\n"))
# rating = float(input("Digite a nota de avaliação do filme: \n"))

# if rating > 8.0 and yearRelease > 2015:
#     print(f"O filme {name} é muito bom, recomendo!")
# else:
#     print(f"O filme {name} não é recomendado")

num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
operation = input("Digite a operação a ser realizada: (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação inválida")
    result = 0
    
print(result)