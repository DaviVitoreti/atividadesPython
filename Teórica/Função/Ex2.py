def ler_valor():
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    z = int(input("Digite o terceiro valor: "))
    return x, y, z 

def soma(x, y, z):
    soma = x + y + z
    return soma

x, y, z = ler_valor()
soma = soma(x, y, z)
print(f"soma = {soma}")