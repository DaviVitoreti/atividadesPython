a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))
e = int(input("Digite o valor de e: "))
f = int(input("Digite o valor de f: "))

testeZero = a * b * c * d

while (testeZero == 0):
    if (a == 0):
        a = int(input("Digite um valor válido para a: "))
    elif (b == 0):
        b = int(input("Digite um valor válido para b: "))
    elif (c == 0):
        c = int(input("Digite um valor válido para c: "))
    elif (d == 0):
        d = int(input("Digite um valor válido para d: "))
        testeZero = a * b * c * d
else:
    x = (c*e - b*f) / (a*e - b*d)
    y = (a*f - c*d) / (a*e - b*d)
    if (x < 0):
        print(f"x = {x}")
        print("O sistema não tem solução")
    elif (y < 0):
        print(f"y = {y}")
        print("O sistema não tem solução")
    else:
        print(f"x = {x}")
        print(f"y = {y}")