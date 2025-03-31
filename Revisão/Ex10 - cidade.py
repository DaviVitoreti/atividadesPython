pop = 0
ms = 0
mf = 0
maiorS = -1
cont = 0

sal = float(input("Salario: "))
while (sal >= 0):
    pop = pop + 1
    ms += ms
    filhos = int(input("N° de filhos: "))
    mf = mf + filhos
    if (sal > maiorS):
        maiorS = sal
    if (sal < 1500):
        cont = cont + 1
    sal = float(input("Salario: "))

ms = ms / pop
mf = mf // pop
perc = (cont/pop) * 100

print(f"Total da população: {pop}")
print(f"Salário médio: R${ms:.2f}")
print(f"Número médio de filhos: {mf}")
print(f"Maior salário: R${maiorS:.2f}")
print(f"Percentual de pessoas com salário menor que R$1500,00: {perc:.2f}%")