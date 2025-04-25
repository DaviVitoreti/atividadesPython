print(f"// Calculadora de Nota //")
num_alunos = int(input("Digite a quantidade de alunos que serão inseridos: "))
cont_MFmaior5 = 0
buscar_nome = ""
menu = ""
boletim_sala = []
notaMF_maior = ["", -1]
menorMF = ["", 0]

for x in range(num_alunos):
    boletim_aluno = []
    notaT = []
    notaP = []
    notaMT_MP = []
    print(f"\n-- {x+1}° Aluno --")
    nome = input(f"Digite o nome do aluno: ")
    nome = nome.title()
    notaT1 = float(input("Digite a nota da prova teórica T1: "))
    notaT2 = float(input("Digite a nota da prova teórica T2: "))
    notaP1 = float(input("Digite a nota do projeto P1: "))
    notaP2 = float(input("Digite a nota do projeto P2: "))

    notaMT = 0.4*notaT1 + 0.6*notaT2
    notaMP = (notaP1+notaP2)/2

    if (notaMT > 5):
        if (notaMP > 5):
            notaMF = 0.3*notaMP + 0.7*notaMT
            cont_MFmaior5 += 1
        else:
            notaMF = notaMP
    else:
        if (notaMT < notaMP):
            notaMF = notaMT
        else:
            notaMF = notaMP 

    boletim_aluno.append(nome)
    notaT.append(notaT1)
    notaT.append(notaT2)
    boletim_aluno.append(notaT)
    notaP.append(notaP1)
    notaP.append(notaP2)
    boletim_aluno.append(notaP)
    notaMT_MP.append(notaMT)
    notaMT_MP.append(notaMP)
    boletim_aluno.append(notaMT_MP)
    boletim_aluno.append(notaMF)
    boletim_sala.append(boletim_aluno)

for x in range(num_alunos):
    if (boletim_sala[x][4] > notaMF_maior[1]):
        if (x == 0):
            menorMF[0] = boletim_sala[x][0]
            menorMF[1] = boletim_sala[x][4]
        notaMF_maior[0] = boletim_sala[x][0]
        notaMF_maior[1] = boletim_sala[x][4]
    else:
        menorMF[0] = boletim_sala[x][0]
        menorMF[1] = boletim_sala[x][4]

perc_MFmaior5 = (cont_MFmaior5 / num_alunos) * 100

print("\n// Menu de Opções //")
print("1. Um boletim da sala, contendo de cada aluno o nome, Média Teórica (MT), Média Prática (MP) e Média Final (MF).")
print("2. Buscar o boletim de um aluno em específico.")
print("3. O aluno com a maior Média Final (MF).")
print("4. O aluno com a menor Média Final (MF).")
print("5. O percentual de Média Final (MF) superior a 5,0.")
print("\nDigite o número correspondente a cada opção para buscar.\nDigite \"Sair\" para encerrar o programa.")
print("Digite \"Menu\" para consultar o menu de opções novamente.")
while (menu != "Sair"):
    menu = input("< Menu >: ")
    menu = menu.title()

    if (menu != "Sair"):
        if (menu == "Menu"):
            print("\n// Menu de Opções //")
            print("1. Um boletim da sala, contendo de cada aluno o nome, Média Teórica (MT), Média Prática (MP) e Média Final (MF).")
            print("2. Buscar o boletim de um aluno em específico.")
            print("3. O aluno com a maior Média Final (MF).")
            print("4. O aluno com a menor Média Final (MF).")
            print("5. O percentual de Média Final (MF) superior a 5,0.")
        else:
            if (menu == "1"):
                print("\n// Boletim da Sala //")
                print("Nome\tMT\tMP\tMF")
                for x in range(num_alunos):
                    print(f"{boletim_sala[x][0]}\t{boletim_sala[x][3][0]:.2f}\t{boletim_sala[x][3][1]:.2f}\t{boletim_sala[x][4]:.2f}")
            elif (menu == "2"):
                print("\n// Buscar Aluno //")
                print("Digite o nome do aluno para buscar o seu boletim\nCaso queira sair, digite \"Sair\"")
                while (buscar_nome != "Sair"):
                    buscar_nome = input("< Nome >: ")
                    buscar_nome = buscar_nome.title()
                    busca_control = 0
                    if (buscar_nome != "Sair"):
                        for x in range(num_alunos):
                            if (boletim_sala[x][0] == buscar_nome):
                                print(f"\n// Boletim de {boletim_sala[x][0]} //")
                                print("Nome\tT1\tT2\tP1\tP2\tMT\tMP\tMF")
                                print(f"{boletim_sala[x][0]}\t{boletim_sala[x][1][0]:.2f}\t{boletim_sala[x][1][1]:.2f}\t{boletim_sala[x][2][0]:.2f}\t{boletim_sala[x][2][1]:.2f}\t{boletim_sala[x][3][0]:.2f}\t{boletim_sala[x][3][1]:.2f}\t{boletim_sala[x][4]:.2f}\n")
                            else:
                                busca_control += 1
                    if (busca_control == num_alunos):
                        print("Não foi possível encontrar o aluno.\nVerifique se digitou o nome corretamente.")
            elif (menu == "3"):
                print(f"O aluno(a) {notaMF_maior[0]} obteve a maior Média Final, sendo: {notaMF_maior[1]:.2f}\n")
            elif (menu == "4"):
                print(f"O aluno(a) {menorMF[0]} obteve a menor Média Final, sendo: {menorMF[1]:.2f}\n")
            elif (menu == "5"):
                print(f"O percentual de alunos com Média Final superior a 5 é: {perc_MFmaior5:.2f}%\n")
            else:
                print("Opção inválida, por favor, tente novamente\n")