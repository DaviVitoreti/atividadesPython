x = int(input("Digite um valor qualquer: "))
y = x % 5
z = x % 3

if (y == 0):
    if (z == 0):
        print("O valor",x,"é divisivel por 5 e 3")
    else:
        print("O valor",x,"não é divisivel por 3")
elif (z == 0):
    print("O valor",x,"não é divisivel por 5")
else:
    print("O valor",x,"não é divisivel nem por 5 e nem por 3")