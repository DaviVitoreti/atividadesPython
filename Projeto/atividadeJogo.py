import random
tentativas = 10

primer_dig_control = 0
segun_dig_control = 0
ter_dig_control = 0
quar_dig_control = 0

numero_aleatorio = random.randint(1000,9999)

primeiro_digito = numero_aleatorio % 10
segundo_digito = (numero_aleatorio // 10) % 10
terceiro_digito = (numero_aleatorio // 100) % 10
quarto_digito = (numero_aleatorio // 1000) % 10

print(f"// Jogo da Adivinhação //")
print(f"O número gerado está entre 1000 e 9999")

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
            primer_dig_control += 1
            acertos += 1
    if (segun_dig_control == 0):
        if (segundo_digito_tentativa == segundo_digito):
            segundo_digito_correto = segundo_digito
            segun_dig_control += 1
            acertos += 1
    if (ter_dig_control == 0):
        if (terceiro_digito_tentativa == terceiro_digito):
            terceiro_digito_control = terceiro_digito
            ter_dig_control += 1
            acertos += 1
    if (quar_dig_control == 0):
        if (quarto_digito_tentativa == quarto_digito):
            quarto_digito_control = quarto_digito
            quar_dig_control += 1
            acertos += 1

    tentativas -= 1

    if (acertos == 0):
        print(f"Você não acertou nenhum digto.")
    else:
        print(f"Você acertou {acertos} digitos.")
    print(f"Restam {tentativas} tentativas.")
    print(f"Seu número é: ")