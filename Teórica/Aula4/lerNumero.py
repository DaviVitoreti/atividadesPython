x = int(input("Digite um número em 100 e 1000: "))

if (x >= 100) and (x <= 1000):
    if (x <= 250):
        print("1°")
    elif (x <= 500):
        print("2°")
    elif (x <= 750):
        print("3°")
    else:
        print("4°")
else:
    print("Fora do escopo")