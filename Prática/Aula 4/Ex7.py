num = 0
contImpar = 0
contPar = 0

while (num > 0):
    num = int(input("Digite um número: "))
    if (num%2 == 0):
        contPar += 1
    else:
        contImpar += 1