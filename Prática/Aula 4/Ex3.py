numMax = -999999999
const = 1

while (const <= 10):
    num = float(input("Digite um outro valor: "))
    if (num > numMax):
        numMax = num
    const += 1
else:
    print(f"O maior valor é: {numMax}")