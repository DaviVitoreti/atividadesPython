num = int(input("Digite um número: "))
print(f"\nOs divisores de {num} são: ",end=" ")

for div in range(1, (num+1)):
    if(num%div == 0):
        print(div,end=" ")
print("\n")