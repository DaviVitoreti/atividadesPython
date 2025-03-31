x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

if (x > y):
    if (x > z):
        print(f"\n{x} é o maior valor")
    else:
        print(f"\n{z} é o maior valor")
elif (y > z):
    print(f"\n{y} é o maior valor")
else:
    print(f"\n{z} é o maior valor")