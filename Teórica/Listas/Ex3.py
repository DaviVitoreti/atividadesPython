x = []
maior = -999999999

for i in range(10):
    aux = float(input(f"Digite o {i+1}° número: "))
    x.append(aux)
    soma = x[0] + x[i]

    if (x[i] > maior):
        maior = x[i]
    else:
        menor = x[i]

    if (x[i] > 29):
        cont_maior_29 += 1

media = soma / 10

print(f"\n// Resultados //")
print(f"Média: {media}")
print(f"Número maior: {maior}")
print(f"Número menor: {menor}")
print(f"Quantidade de números maiores que 29: {cont_maior_29}")
print(f"A lista é: {x}")