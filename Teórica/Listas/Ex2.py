x = []

for i in range(15):
    aux = int(input(f"Digite o {i+1}° número: "))
    x.append(aux)

cont = int(input("\nDigite o número que você deseja procurar na lista: "))

if (x.count(cont) != 0):
    print(f"O número {cont} existe na lista")
else:
    print(f"O número {cont} não existe na lista")
