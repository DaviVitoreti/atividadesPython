nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nome_completo = nome + " " + sobrenome

print(f"\nO nome completo é: {nome_completo}")
print(f"O nome contém {len(nome_completo)} caracteres")
print(f"O primerio e ultimo caracteres são, respectivamente: \"{nome_completo[0]}\" e \"{nome_completo[-1]}\"")
