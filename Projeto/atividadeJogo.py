import random
numero_aleatorio = random.randint(1000,9999)

primeiro_digito = numero_aleatorio % 10
segundo_digito = (numero_aleatorio // 10) % 10
terceiro_digito = (numero_aleatorio // 100) % 10
quarto_digito = (numero_aleatorio // 1000) % 10

tentativas = 10
vitoria = 0
dica_control = 0
primer_dig_control = 0
segun_dig_control = 0
ter_dig_control = 0
quar_dig_control = 0

print(f"\n// Jogo da Adivinhação //")
print(f"O número gerado está entre 1000 e 9999")
print(f"Você possui 10 tentativas para encontrar o número")

while (vitoria < 4):
    while (tentativas > 0):
        num_digitado = int(input(f"< Digite um valor >: "))
        acertos = 0
        primeiro_digito_tentativa = num_digitado % 10
        segundo_digito_tentativa = (num_digitado // 10) % 10
        terceiro_digito_tentativa = (num_digitado // 100) % 10
        quarto_digito_tentativa = (num_digitado // 1000) % 10

        if (num_digitado < 1000):
            print(f"\n// ERRO! //")
            print(f"O número digitado é inválido!")
            print(f"Lembre-se que o número gerado está entre 1000 e 9999")
            print(f"Essa tentativa não será considerada.")
            tentativas += 1
        elif (num_digitado > 9999):
            print(f"\n// ERRO! //")
            print(f"O número digitado é inválido!")
            print(f"Lembre-se que o número gerado está entre 1000 e 9999")
            print(f"Essa tentativa não será considerada.")
            tentativas += 1
        else:
            print("\nSeu número é:",end=" ")
            if (quar_dig_control == 0):
                if (quarto_digito_tentativa == quarto_digito):
                    print(quarto_digito,end=" ")
                    quar_dig_control += 1
                    acertos += 1
                    vitoria += 1
                else:
                    print("_",end=" ")
            else:
                print(quarto_digito,end=" ")
            if (ter_dig_control == 0):
                if (terceiro_digito_tentativa == terceiro_digito):
                    print(terceiro_digito,end=" ")
                    ter_dig_control += 1
                    acertos += 1
                    vitoria += 1
                else:
                    print("_",end=" ")
            else:
                print(terceiro_digito,end=" ")
            if (segun_dig_control == 0):
                if (segundo_digito_tentativa == segundo_digito):
                    print(segundo_digito,end=" ")
                    segun_dig_control += 1
                    acertos += 1
                    vitoria += 1
                else:
                    print("_",end=" ")
            else:
                print(segundo_digito,end=" ")
            if (primer_dig_control == 0):
                if (primeiro_digito_tentativa == primeiro_digito):
                    print(primeiro_digito,end=" ")
                    primer_dig_control += 1
                    acertos += 1
                    vitoria += 1
                else:
                    print("_",end=" ")
            else:
                print(primeiro_digito,end=" ")

        tentativas -= 1

        if (acertos == 0):
            print(f"\nVocê não acertou nenhum digito.")
        else:
            print(f"\nVocê acertou {acertos} digitos.")
        print(f"Restam {tentativas} tentativas.")
        if (tentativas == 5) or (tentativas == 3):
            if (primer_dig_control == 0) and (dica_control == 0):
                dica_control += 1
                if (primeiro_digito%2 == 0):
                    print(f"\n// DICA! //")
                    print(f"O primeiro digito é PAR.")
                elif (primeiro_digito < 5):
                    print(f"\n// DICA! //")
                    print(f"O primeiro digito é menor que 5.")
                else:
                    print(f"\n// DICA! //")
                    print(f"O primeiro digito é maior ou igual a 5.")
            if (segun_dig_control == 0) and (dica_control == 0):
                dica_control += 1
                if (segundo_digito%2 == 0):
                    print(f"\n// DICA! //")
                    print(f"O segundo digito é PAR.")
                elif (segundo_digito < 5):
                    print(f"\n// DICA! //")
                    print(f"O segundo digito é menor que 5.")
                else:
                    print(f"\n// DICA! //")
                    print(f"O segundo digito é maior ou igual a 5.")
            if (ter_dig_control == 0) and (dica_control == 0):
                dica_control += 1
                if (terceiro_digito%2 == 0):
                    print(f"\n// DICA! //")
                    print(f"O terceiro digito é PAR.")
                elif (terceiro_digito < 5):
                    print(f"\n// DICA! //")
                    print(f"O terceiro digito é menor que 5.")
                else:
                    print(f"\n// DICA! //")
                    print(f"O terceiro digito é maior ou igual a 5.")
            if (quar_dig_control == 0) and (dica_control == 0):
                dica_control += 1
                if (quarto_digito%2 == 0):
                    print(f"\n// DICA! //")
                    print(f"O quarto digito é PAR.")
                elif (quarto_digito < 5):
                    print(f"\n// DICA! //")
                    print(f"O quarto digito é menor que 5.")
                else:
                    print(f"\n// DICA! //")
                    print(f"O quarto digito é maior ou igual a 5.")
        ctrl_dica = 1

        if (vitoria >= 4):
            print(f"\n// Fim de Jogo //")
            print(f"Você ganhou o jogo!")
            print(f"Código: {numero_aleatorio}")
            print(f"Em {10 - tentativas} tentativas")
            voltarJogo = int(input("Você quer jogar novamente? Digite \"1\" para continuar: "))
            if (voltarJogo == 1):
                tentativas = 10
                vitoria = 0
                voltarJogo = 0
                primer_dig_control = 0
                segun_dig_control = 0
                ter_dig_control = 0
                quar_dig_control = 0
                numero_aleatorio = random.randint(1000,9999)
                primeiro_digito = numero_aleatorio % 10
                segundo_digito = (numero_aleatorio // 10) % 10
                terceiro_digito = (numero_aleatorio // 100) % 10
                quarto_digito = (numero_aleatorio // 1000) % 10
                print(f"\n// Jogo da Adivinhação //")
                print(f"O número gerado está entre 1000 e 9999")
                print(f"Você possui 10 tentativas para encontrar o número")
            else:
                tentativas = 0
                vitoria = 5
        elif (tentativas == 0):
            print(f"\n// Fim de Jogo //")
            print(f"Você perdeu o jogo por falta de tentativas.")
            print(f"O código era: {numero_aleatorio}")
            voltarJogo = int(input("Você quer jogar novamente? Digite \"1\" para continuar: "))
            if (voltarJogo == 1):
                tentativas = 10
                vitoria = 0
                voltarJogo = 0
                primer_dig_control = 0
                segun_dig_control = 0
                ter_dig_control = 0
                quar_dig_control = 0
                numero_aleatorio = random.randint(1000,9999)
                primeiro_digito = numero_aleatorio % 10
                segundo_digito = (numero_aleatorio // 10) % 10
                terceiro_digito = (numero_aleatorio // 100) % 10
                quarto_digito = (numero_aleatorio // 1000) % 10
                print(f"\n// Jogo da Adivinhação //")
                print(f"O número gerado está entre 1000 e 9999")
                print(f"Você possui 10 tentativas para encontrar o número")
            else:
                tentativas = 0
                vitoria = 5