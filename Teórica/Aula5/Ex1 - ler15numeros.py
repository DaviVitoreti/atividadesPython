num = int(input("Digite o 1° número: "))
maior = num
cont = 1

while (cont < 15):
    num = int(input(f"Digite o {cont + 1}° número: "))
    cont = cont + 1
    if (num > maior):
        maior = num
else:
    print(f"O maior número é: {maior}")