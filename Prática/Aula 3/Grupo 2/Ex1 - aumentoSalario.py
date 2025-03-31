plano = int(input("Digite o plano de trabalho do funcionário: "))
salarioAtual = float(input("Digite o salário atual do funcionário: "))

while (plano > 3) or (plano == 0):
    plano = int(input("Digite um plano de trabalho válido: "))
else:
    if (plano == 1):
        salarioNovo = salarioAtual * 1.1
        print(f"O novo salário será de: R$ {salarioNovo:.2f}")
    elif (plano == 2):
        salarioNovo = salarioAtual * 1.15
        print(f"O novo salário será de: R$ {salarioNovo:.2f}")
    else:
        salarioNovo = salarioAtual * 1.2
        print(f"O salário novo será de: R$ {salarioNovo:.2f}")