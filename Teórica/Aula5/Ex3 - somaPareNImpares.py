quant = int(input("Digite a quantidade de números a ser lida: "))
somaPar = 0
contImpar = 0

for cont in range(quant):
    num = int(input("Digite um valor: "))
    if(num%2 == 0):
        somaPar = somaPar + num
    else:
        contImpar = contImpar + 1
print(f"A soma dos pares lidos é {somaPar}")
print(f"Foram lidos {contImpar} números impares")