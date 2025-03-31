num = int(input("Digite um número: "))
print(f"\nOs divisores de {num} são: ",end=" ")
div = 1

while (div <= 1):
    if(num%div == 0):
        print(div,end=" ")
    div = div + 1
print("\n")