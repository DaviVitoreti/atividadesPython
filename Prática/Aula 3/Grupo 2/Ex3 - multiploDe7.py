num = 100

while (num >= 100) and (num <= 450):
    mul7 = num % 7
    if (mul7 == 0):
        print(num)
        num = num + 1
    else:
        num = num + 1
else:
    print("Fim do programa")