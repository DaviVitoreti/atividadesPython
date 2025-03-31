x = int(input("Digite um valor: "))
y = int(input("Digite outro valor: "))
z = x / y

if (z != 1):
    if (z > 1):
        print("O maior valor é: ",x)
    else:
        print("O maior valor é: ",y)
else:
    print("Os dois valores são iguais")