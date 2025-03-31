import random
numero_aleatorio = random.randint(1000,9999)

# Divisão dos 4 digitos em variáveis separadas
primeiro_digito = numero_aleatorio % 10
segundo_digito = (numero_aleatorio // 10) % 10
terceiro_digito = (numero_aleatorio // 100) % 10
quarto_digito = (numero_aleatorio // 1000) % 10

tentativas = 10
vitoria = 0
voltarJogo = ""
ctrl_dica = 1
primer_dig_control = 0
segun_dig_control = 0
ter_dig_control = 0
quar_dig_control = 0

Digito1 = "_"
Digito2 = "_"
Digito3 = "_"
Digito4 = "_"

print(f"// Jogo da Adivinhação //")
print(f"O número gerado está entre 1000 e 9999")

while (vitoria < 4):
    while (tentativas > 0):
        num_digitado = int(input(f"< Digite um valor >: "))
        acertos = 0
        primeiro_digito_tentativa = num_digitado % 10
        segundo_digito_tentativa = (num_digitado // 10) % 10
        terceiro_digito_tentativa = (num_digitado // 100) % 10
        quarto_digito_tentativa = (num_digitado // 1000) % 10

        if (num_digitado < 1000):
            print(f"O número {num_digitado} é inválido!")
            print(f"Essa tentativa não será considerada.")
            print(f"Por favor, tente novamente: ")
            tentativas += 1
        elif (num_digitado > 9999):
                print(f"O número {num_digitado} é inválido!")
                print(f"Essa tentativa não será considerada.")
                print(f"Por favor, tente novamente: ")
                tentativas += 1

        if (primer_dig_control == 0):
            if (primeiro_digito_tentativa == primeiro_digito):
                primeiro_digito_correto = primeiro_digito_tentativa
                Digito1 = primeiro_digito_tentativa
                primer_dig_control += 1
                acertos += 1
                vitoria += 1
        if (segun_dig_control == 0):
            if (segundo_digito_tentativa == segundo_digito):
                segundo_digito_correto = segundo_digito
                Digito2 = segundo_digito_tentativa
                segun_dig_control += 1
                acertos += 1
                vitoria += 1
        if (ter_dig_control == 0):
            if (terceiro_digito_tentativa == terceiro_digito):
                terceiro_digito_control = terceiro_digito
                Digito3 = terceiro_digito_tentativa
                ter_dig_control += 1
                acertos += 1
                vitoria += 1
        if (quar_dig_control == 0):
            if (quarto_digito_tentativa == quarto_digito):
                quarto_digito_control = quarto_digito
                Digito4 = quarto_digito_tentativa
                quar_dig_control += 1
                acertos += 1
                vitoria += 1

        tentativas -= 1

        if (acertos == 0):
            print(f"\nVocê não acertou nenhum digito.")
        else:
            print(f"\nVocê acertou {acertos} digitos.")
        if (tentativas == 5) or (tentativas == 3):
            if (Digito1 == "_") and (ctrl_dica != 0):
                ctrl_dica = 0
                if (primeiro_digito%2 == 0):
                    Digito1 = "PAR"
                    print(f"Dica: O primeiro digito é PAR.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
                elif (primeiro_digito < 5):
                    Digito1 = "<5"
                    print(f"Dica: O primeiro digito é menor que 5.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
                else:
                    Digito1 = ">=5"
                    print(f"Dica: O primeiro digito é maior ou igual a 5.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
            if (Digito2 == "_") and (ctrl_dica != 0):
                ctrl_dica = 0
                if (segundo_digito%2 == 0):
                    Digito2 = "PAR"
                    print(f"Dica: O segundo digito é PAR.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
                elif (segundo_digito < 5):
                    Digito2 = "<5"
                    print(f"Dica: O segundo digito é menor que 5.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
                else:
                    Digito2 = ">=5"
                    print(f"Dica: O segundo digito é maior ou igual a 5.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
            if (Digito3 == "_") and (ctrl_dica != 0):
                ctrl_dica = 0
                if (terceiro_digito%2 == 0):
                    Digito3 = "PAR"
                    print(f"Dica: O terceiro digito é PAR.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
                elif (terceiro_digito < 5):
                    Digito3 = "<5"
                    print(f"Dica: O terceiro digito é menor que 5.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
                else:
                    Digito3 = ">=5"
                    print(f"Dica: O terceiro digito é maior ou igual a 5.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
            if (Digito4 == "_") and (ctrl_dica != 0):
                ctrl_dica = 0
                if (quarto_digito%2 == 0):
                    Digito4 = "PAR"
                    print(f"Dica: O quarto digito é PAR.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
                elif (quarto_digito < 5):
                    Digito4 = "<5"
                    print(f"Dica: O quarto digito é menor que 5.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
                else:
                    Digito4 = ">=5"
                    print(f"Dica: O quarto digito é maior ou igual a 5.")
                    print(f"Restam {tentativas} tentativas.")
                    print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")
        else:
            print(f"Restam {tentativas} tentativas.")
            print(f"Seu número é: {Digito4} {Digito3} {Digito2} {Digito1}")

        ctrl_dica = 1

        if (tentativas == 0):
            print(f"\n// Fim de Jogo //")
            print(f"Você perdeu o jogo por falta de tentativas.")
            print(f"O código era: {numero_aleatorio}")
            voltarJogo = input("Você quer jogar novamente? S/N: ")
            if (voltarJogo == "S"):
                tentativas = 10
                vitoria = 0
                voltarJogo = ""
                primer_dig_control = 0
                segun_dig_control = 0
                ter_dig_control = 0
                quar_dig_control = 0
                Digito1 = "_"
                Digito2 = "_"
                Digito3 = "_"
                Digito4 = "_"

                numero_aleatorio = random.randint(1000,9999)
                primeiro_digito = numero_aleatorio % 10
                segundo_digito = (numero_aleatorio // 10) % 10
                terceiro_digito = (numero_aleatorio // 100) % 10
                quarto_digito = (numero_aleatorio // 1000) % 10
            else:
                tentativas = 0
                vitoria = 5
        elif (vitoria == 4):
            print(f"\n// Fim de Jogo //")
            print(f"Você ganhou o jogo!")
            print(f"Código: {numero_aleatorio}")
            print(f"Em {10 - tentativas} tentativas")
            voltarJogo = input("Você quer jogar novamente? \nDigite \"S\" para continuar: ")
            print("\n")
            if (voltarJogo == "S"):
                tentativas = 10
                vitoria = 0
                voltarJogo = ""
                primer_dig_control = 0
                segun_dig_control = 0
                ter_dig_control = 0
                quar_dig_control = 0
                Digito1 = "_"
                Digito2 = "_"
                Digito3 = "_"
                Digito4 = "_"

                numero_aleatorio = random.randint(1000,9999)
                primeiro_digito = numero_aleatorio % 10
                segundo_digito = (numero_aleatorio // 10) % 10
                terceiro_digito = (numero_aleatorio // 100) % 10
                quarto_digito = (numero_aleatorio // 1000) % 10
            else:
                tentativas = 0
                vitoria = 5