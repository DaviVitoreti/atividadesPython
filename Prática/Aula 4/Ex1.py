n = int(input("Digite um valor: "))
t1 = 0
t2 = 0
t3 = 0
t4 = 0

while (n >= 0):
    if (n <= 25):
        t1 += 1
    elif (n <= 50):
        t2 += 1
    elif (n <= 75):
        t3 += 1
    elif (n <= 100):
        t4 += 1
    else:
        print("Invalido")
    n = int(input("Digite um outro valor: "))
else:
    print(f"Quantidade de N° entre 0 e 25: {t1}")
    print(f"Quantidade de N° entre 26 e 50: {t2}")
    print(f"Quantidade de N° entre 51 e 75: {t3}")
    print(f"Quantidade de N° entre 76 e 100: {t4}")