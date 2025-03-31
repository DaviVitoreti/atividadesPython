num = int(input("Digite um número: "))
menor = num

while (num > 0):
    if (num < menor):
        menor = num
    num = int(input("Digite um outro número: "))
else:
    print(f"O menor número é: {menor}")
