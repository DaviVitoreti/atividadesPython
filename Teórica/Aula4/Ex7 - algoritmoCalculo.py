x = float(input("Digite um valor inteiro qualquer: "))

if (x != 1):
    if (x < 1):
        y = x
        print("y =",y)
    else:
        y = x ** x
        print("y =",y)    
else:
    y = 0
    print("y =",y)