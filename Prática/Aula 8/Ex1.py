pessoas = {}
cont = 1
buscar_nome = ""

while (cont <= 3):
    print(f"\n-- {cont}° Cadastro --")
    nome = input("Digite o seu nome: ")
    nome = nome.title()
    if (nome in pessoas.keys()):
        print("O nome já existe.")
    else:
        idade = input("Digite a sua idade: ")
        cidade = input("Digite a sua cidade: ")
        cidade = cidade.title()
        pessoas[nome]=[idade,cidade]
        print(pessoas)
        cont += 1

print("\nDigite o nome a ser procurado, ou digite \"Sair\" para sair.")
while (buscar_nome != "Sair"):
    buscar_nome = input("< Nome>: ")
    buscar_nome = buscar_nome.title()
    if (buscar_nome != "Sair"):
        if (buscar_nome in pessoas.keys()):
            print(f"Valores = {pessoas[buscar_nome]}")
        else:
            print("Não foi possível encontrar o nome")