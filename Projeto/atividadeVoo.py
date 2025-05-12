usuarios = {}
voo = {}
passageiros = []
id = 1
menu = ""
    
# Função para cadastrar um novo usuário
def cadastro_usuario():
    menu = ""
    while (menu != "N"):
        cpf = input("Digite o seu CPF: ")
        while (cpf in usuarios.keys()):
            print("Esse CPF já está cadastrado.")
            cpf = input("Digite o seu CPF: ")
        nome = input("Digite o seu nome: ")
        telefone = input("Digite o seu telefone (XX)(XXXXX-XXXX): ")
        usuarios[cpf] = [nome, telefone]
        print(f"Usuário cadastrado com sucesso!")
        menu = input("Digite \"N\" para sair ou digite qualquer tecla para continuar\nDeseja cadastrar outro usuário?")
        menu = menu.title()

# Função para cadastrar um novo voo
def cadastro_voo(id):
    menu = ""
    while (menu != "N"):
        origem = input("Digite o local de origem: ")
        destino = input("Digite o local de destino: ")
        escala = int(input("Digite quantas escalas o voo possui: "))
        preco = float(input("Digite o preço da passagem (R$XXXX.xx): "))
        lugar = int(input("Digite a quantidade de lugares disponíveis: "))
        voo[id] = [origem, destino, escala, preco, lugar]
        print(f"Voo cadastrado com sucesso!")
        menu = input("Digite \"N\" para sair ou digite qualquer tecla para continuar\nDeseja cadastrar outro voo?")
        menu = menu.title()

# Função para vender passagens
def venda_passagem():
    cpf = input("Digite o CPF do passageiro: ")
    if (cpf in usuarios.keys()):
        codigo = int(input("Digite o código do voo: "))
        if (codigo in voo.keys()):
            if (voo[codigo][4] > 0):
                print(f"Passagem vendida com sucesso para {usuarios[cpf][0]}!")
                voo[codigo][4] -= 1
                passageiros.append([codigo, usuarios[cpf][0]])
            else:
                print("Não há lugares disponíveis.")
        else:
            print("Voo não encontrado.")
    else:
        print("Usuário não encontrado.")

# Função para listar os voos
def listar_voo(i):
    print(f"Código de Voo: {i[0]}")
    print(f"Origem: {i[1][0]}")
    print(f"Destino: {i[1][1]}")
    print(f"Escalas: {i[1][2]}")
    print(f"Preço: {i[1][3]}")
    print(f"Lugares disponíveis: {i[1][4]}\n")

# Função para mostrar o menu
def menu():
    print("// Sistema de Passagem //")
    print("1. Cadastrar um novo usuário.")
    print("2. Cadastrar um novo voo.")
    print("3. Consultar um voo.")
    print("4. Informar o voo com menor escala.")
    print("5. Venda de passagem.")
    print("6. Listar os passageiros em um voo.")
    print("Digite \"Sair\" para encerrar o programa.\nDigite \"Menu\" para consultar o menu de opções novamente.")

# Função para consultar voos
def consulta_voo(consulta):
    if (consulta == "1"):
        codigo = int(input("Digite o código do voo: "))
        if (codigo in voo.keys()):
            print("\n// Voo //")
            print(f"Código do Voo: {codigo}")
            print(f"Origem: {voo[codigo][0]}")
            print(f"Destino: {voo[codigo][1]}")
            print(f"Escalas: {voo[codigo][2]}")
            print(f"Preço: {voo[codigo][3]}")
            print(f"Lugares disponíveis: {voo[codigo][4]}\n")
        else:
            print("Voo não encontrado.")
    elif (consulta == "2"):
        origem = input("Digite a cidade de origem: ")
        origem = origem.title()
        for i in voo.items():
            if (i[1][0] == origem):
                listar_voo(i)
            else:
                print("Voo não encontrado.")
    elif (consulta == "3"):
        destino = input("Digite a cidade de destino: ")
        destino = destino.title()
        for i in voo.items():
            if (i[1][1] == destino):
                listar_voo(i)
            else:
                print("Voo não encontrado.")

# Função para informar o voo com menor escala
def menor_escala(origem, destino):
    menor = 999999
    for i in voo.items():
        if (i[1][0] == origem and i[1][1] == destino):
            if (i[1][2] < menor):
                menor = i[1][2]
                voo_menor_escala = i
    print(f"// Voo com menor escala //")
    listar_voo(voo_menor_escala)

# Menu de opções
menu()
while (menu != "Sair"):
    menu = input("< Menu >: ")
    menu = menu.title()

    if (menu != "Sair"):
        if (menu == "Menu"):
            menu()
        elif (menu == "1"):
            cadastro_usuario()
        elif (menu == "2"):
            cadastro_voo(id)
            id += 1
        elif (menu == "3"):
            consulta = ""
            while (consulta != "Sair"):
                print("O voo pode ser consultado pelo:\n1. Código do voo;\n2. Cidade de origem;\n3. Cidade de destino.")
                print("Digite o número correspondente.\nDigite \"Sair\" para encerrar o programa.")
                consulta = input("< Consulta >: ")
                consulta_voo(consulta)
        elif (menu == "4"):
            menu_escala = ""
            print("// Voo com menor escala //")
            print("O voo pode ser consultado pela cidade de origem e destino.")
            print("Digite \"Sair\" para encerrar o programa.")
            while (menu_escala != "Sair"):
                menu_origem = input("Digite a cidade de origem: ")
                menu_destino = input("Digite a cidade de destino: ")
                menu_origem = menu_origem.title()
                menu_destino = menu_destino.title()
                menor_escala(menu_origem, menu_destino)

                menu_escala = input("Digite \"Sair\" para encerrar o programa.\nDigite qualquer tecla para continuar: ")
                menu_escala = menu_escala.title()
        elif (menu == "5"):
            print("// Venda de Passagem //")
            venda_passagem()