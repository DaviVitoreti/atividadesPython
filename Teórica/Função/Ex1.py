def sucessor_antecessor(num):
    x = num + 1
    y = num - 1
    return x, y

num = int(input("Digite um número: "))
suc, ant = sucessor_antecessor(num)
print(f"Sucessor = {suc}\nAntecessor = {ant}")