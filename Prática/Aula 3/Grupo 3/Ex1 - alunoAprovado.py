N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))

print("\nDigite os pesos a seguir de modo que a soma deles seja igual a 1")
P1 = float(input("Digite o primeiro peso: "))
P2 = float(input("Digite o segundo peso: "))

testePeso = P1 + P2

while (testePeso != 1):
    if (P1 != 1):
        P1 = float(input("Insira um primeiro peso válido: "))
        P2 = float(input("Insira um segundo peso válido: "))
        testePeso = P1 + P2
    else:
        P2 = float(input("Insira um segundo peso válido: "))
        testePeso = P1 + P2
else:
    NF = N1*P1 + N2*P2
    if (NF == 10):
        print(f"\nNota Final = {NF}")
        print(f"O aluno foi aprovado com distinção")
    elif (NF >= 7):
        print(f"\nNota Final = {NF}")
        print(f"O aluno foi aprovado")
    else:
        print(f"\nNota Final = {NF}")
        print(f"O aluno foi reprovado")