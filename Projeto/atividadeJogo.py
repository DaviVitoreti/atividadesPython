import random
numero_aleatorio = random.randint(1000,9999)

primeiro_digito = numero_aleatorio % 10
segundo_digito = (numero_aleatorio // 10) % 10
terceiro_digito = (numero_aleatorio // 100) % 10
quarto_digito = (numero_aleatorio // 1000) % 10

tentativas = 10
vitoria = 0
acertos = 0
dica_control = 0
dica1_control = 0
dica2_control = 0
dica3_control = 0
dica4_control = 0
dica_par = 0
dica_maior = 0
dica_menor = 0
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

        while (num_digitado < 1000) or (num_digitado > 9999):
            print(f"\n// ERRO! //")
            print(f"O número digitado é inválido!")
            print(f"Lembre-se que o número gerado está entre 1000 e 9999")
            print(f"Essa tentativa não será considerada.")
            num_digitado = int(input(f"< Digite um valor >: "))
        else:
            primeiro_digito_tentativa = num_digitado % 10
            segundo_digito_tentativa = (num_digitado // 10) % 10
            terceiro_digito_tentativa = (num_digitado // 100) % 10
            quarto_digito_tentativa = (num_digitado // 1000) % 10
            tentativas -= 1

            if (quar_dig_control == 0):
                if (quarto_digito_tentativa == quarto_digito):
                    quar_dig_control += 1
                    acertos += 1
                    vitoria += 1
            if (ter_dig_control == 0):
                if (terceiro_digito_tentativa == terceiro_digito):
                    ter_dig_control += 1
                    acertos += 1
                    vitoria += 1
            if (segun_dig_control == 0):
                if (segundo_digito_tentativa == segundo_digito):
                    segun_dig_control += 1
                    acertos += 1
                    vitoria += 1
            if (primer_dig_control == 0):
                if (primeiro_digito_tentativa == primeiro_digito):
                    primer_dig_control += 1
                    acertos += 1
                    vitoria += 1

        if (tentativas == 5) or (tentativas == 3):
            if (primer_dig_control == 0) and (dica_control == 0):
                dica_control += 1
                dica1_control += 1
                if (primeiro_digito%2 == 0):
                    dica1_control += 1
                    dica_par += 1
                    print(f"\n// DICA! //")
                    print(f"O primeiro digito é PAR.")
                elif (primeiro_digito > 5):
                    dica_maior += 1
                    print(f"\n// DICA! //")
                    print(f"O primeiro digito é maior que 5.")
                else:
                    dica_menor += 1
                    print(f"\n// DICA! //")
                    print(f"O primeiro digito é menor ou igual a 5.")
            if (segun_dig_control == 0) and (dica_control == 0):
                dica_control += 1
                dica2_control += 1
                if (segundo_digito%2 == 0):
                    dica_par += 1
                    print(f"\n// DICA! //")
                    print(f"O segundo digito é PAR.")
                elif (segundo_digito > 5):
                    dica_maior += 1
                    print(f"\n// DICA! //")
                    print(f"O segundo digito é maior que 5.")
                else:
                    dica_menor += 1
                    print(f"\n// DICA! //")
                    print(f"O segundo digito é menor ou igual a 5.")
            if (ter_dig_control == 0) and (dica_control == 0):
                dica_control += 1
                dica3_control += 1
                if (terceiro_digito%2 == 0):
                    dica_par += 1
                    print(f"\n// DICA! //")
                    print(f"O terceiro digito é PAR.")
                elif (terceiro_digito > 5):
                    dica_maior += 1
                    print(f"\n// DICA! //")
                    print(f"O terceiro digito é maior que 5.")
                else:
                    dica_menor += 1
                    print(f"\n// DICA! //")
                    print(f"O terceiro digito é inferior ou igual a 5.")
            if (quar_dig_control == 0) and (dica_control == 0):
                dica_control += 1
                dica4_control += 1
                if (quarto_digito%2 == 0):
                    dica_par += 1
                    print(f"\n// DICA! //")
                    print(f"O quarto digito é PAR.")
                elif (quarto_digito > 5):
                    dica_maior += 1
                    print(f"\n// DICA! //")
                    print(f"O quarto digito é maior que 5.")
                else:
                    dica_menor += 1
                    print(f"\n// DICA! //")
                    print(f"O quarto digito é menor ou igual a 5.")

        if (acertos == 0):
            print(f"\nVocê não acertou nenhum digito.")
        else:
            print(f"\nVocê acertou {acertos} digitos.")
        print(f"Restam {tentativas} tentativas.")

        print("Seu código é:",end=" ")
        if (quar_dig_control == 1):
            print(quarto_digito,end=" ")
        elif (dica4_control == 1):
            if (dica_par >= 1):
                print("PAR",end=" ")
            elif (dica_maior >= 1):
                print(">5",end=" ")
            else:
                print("<=5",end=" ")
        else:
            print("_",end=" ")
        
        if (ter_dig_control == 1):
            print(terceiro_digito,end=" ")
        elif (dica3_control == 1):
            if (dica_par >= 1):
                print("PAR",end=" ")
            elif (dica_maior >= 1):
                print(">5",end=" ")
            else:
                print("<=5",end=" ")
        else:
            print("_",end=" ")
        
        if (segun_dig_control == 1):
            print(segundo_digito,end=" ")
        elif (dica2_control == 1):
            if (dica_par >= 1):
                print("PAR",end=" ")
            elif (dica_maior >= 1):
                print(">5",end=" ")
            else:
                print("<=5",end=" ")
        else:
            print("_",end=" ")

        if (primer_dig_control == 1):
            print(primeiro_digito,end=" ")
        elif (dica1_control == 1):
            if (dica_par >= 1):
                print("PAR",end=" ")
            elif (dica_maior >= 1):
                print(">5",end=" ")
            else:
                print("<=5",end=" ")
        else:
            print("_")

        dica_control = 0
        dica_par = 0
        dica_maior = 0
        dica_menor = 0

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
                dica_control = 0
                dica1_control = 0
                dica2_control = 0
                dica3_control = 0
                dica4_control = 0
                dica_par = 0
                dica_maior = 0
                dica_menor = 0
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
                dica_control = 0
                dica1_control = 0
                dica2_control = 0
                dica3_control = 0
                dica4_control = 0
                dica_par = 0
                dica_maior = 0
                dica_menor = 0
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