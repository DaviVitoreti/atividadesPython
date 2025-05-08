#passageiro[cpf] = [nome, telefone]
#voo[id] = [cidade_origem, cidade_destino, numero_escala, preco, lugar]
#voo = {}
#voo_disponivel = [voo.keys(), voo.values()[4]]

#voo1 = {0: ["Campinas", "New York", "1", "1299.99", 40]}
#for id in range(3):
#    if (voo1[1][4] > 0):
#        voo_disponivel = [i, voo1[1][4]]
#    else:
#        voo1.pop(id)
#
#print(voo_disponivel)

passageiros = {}
voo = {}
id = 1
menu = ""
    
def cadastro_usuario():
    cpf = input("Digite o seu CPF: ")
    nome = input("Digite o seu nome: ")
    telefone = input("Digite o seu telefone (XX)(XXXXX-XXXX): ")
    passageiros[cpf] = [nome, telefone]

while (menu != "N"):
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")
    escala = input("Digite o número de escalas: ")
    preco = float(input("Digite o preço da passagem: "))
    lugares = int(input("Digite o números de lugares disponíveis: "))

    voo[id] = [origem, destino, escala, preco, lugares]

    menu = input("Você deseja cadastrar mais um voo? S/N: ")
    menu = menu.title()