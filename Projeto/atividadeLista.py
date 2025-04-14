num_alunos = int(input("Digite a quantidade de alunos que serão inseridos: "))
boletim_sala = []

for i in range(num_alunos):  
    boletim_aluno = []
    notaT = []
    notaP = []
    notaMT_MP = []
    nome = input(f"\nDigite o nome do {i+1}° aluno: ")
    notaT1 = float(input("Digite a nota da prova teórica T1: "))
    notaT2 = float(input("Digite a nota da prova teórica T2: "))
    notaP1 = float(input("Digite a nota do projeto P1: "))
    notaP2 = float(input("Digite a nota do projeto P2: "))

    notaMT = 0.4*notaT1 + 0.6*notaT2
    notaMP = (notaP1+notaP2)/2

    if (notaMT > 5):
        if (notaMP > 5):
            notaMF = 0.3*notaMP + 0.7*notaMT
        else:
            notaMF = notaMP
    else:
        notaMF = notaMT
    
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

print("\n// Boletim da Sala //")
print("Nome\tT1\tT2\tP1\tP2\tMT\tMP\tMF")
for x in range(num_alunos):
    print(f"{boletim_sala[x][0]}\t{boletim_sala[x][1][0]}\t{boletim_sala[x][1][1]}\t{boletim_sala[x][2][0]}\t{boletim_sala[x][2][1]}\t{boletim_sala[x][3][0]}\t{boletim_sala[x][3][1]}\t{boletim_sala[x][4]}")

buscar_nome = 1
busca_control = 1
print("\n// Buscar Aluno //")
print("Digite o nome do aluno para buscar o seu boletim\nCaso queira sair, digite \"0\"")
while (buscar_nome != "0"):
    buscar_nome = input("< Nome >: ")
    buscar_nome = buscar_nome.title()
    for x in range(num_alunos):
        if (boletim_sala[x][0] == buscar_nome):
            print(f"\n// Boletim de {boletim_sala[x][0]} //")
            print("Nome\tT1\tT2\tP1\tP2\tMT\tMP\tMF")
            print(f"{boletim_sala[x][0]}\t{boletim_sala[x][1][0]}\t{boletim_sala[x][1][1]}\t{boletim_sala[x][2][0]}\t{boletim_sala[x][2][1]}\t{boletim_sala[x][3][0]}\t{boletim_sala[x][3][1]}\t{boletim_sala[x][4]}")
        else:
            busca_control += 1
    if (buscar_nome == num_alunos):
        print("Não possível encontrar o aluno.")

notaMF_maior = [0, -1]
menorMF = [0, 0]
for x in range(num_alunos):
    if (boletim_sala[x][4] > notaMF_maior[1]):
        notaMF_maior[0] = boletim_sala[x][0]
        notaMF_maior[1] = boletim_sala[x][4]
    else:
        menorMF[0] = boletim_sala[x][0]
        menorMF[1] = boletim_sala[x][4]
    
print(f"\nO aluno(a) {notaMF_maior[0]} obteve a maior Média Final, sendo: {notaMF_maior[1]}")
print(f"O aluno(a) {menorMF[0]} obteve a menor Média Final, sendo: {menorMF[1]}")

cont_MFmaior5 = 0
for x in range(num_alunos):
    if (boletim_sala[x][4] > 5):
        cont_MFmaior5 += 1
    perc_MFmaior5 = (cont_MFmaior5 / num_alunos) * 100
print(f"O percentual de alunos com Média Final superior a 5 é: {perc_MFmaior5:.2f}%")
