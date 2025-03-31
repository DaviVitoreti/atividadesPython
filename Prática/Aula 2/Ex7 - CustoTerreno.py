comprimento = float(input("Digite o comprimento do terreno a ser cercado: "))
largura = float(input("Digite a largura do terreno: "))
preço = float(input("Digite o preço do metro de tela: "))

custoPerimetro = (comprimento * 2 + largura * 2) * preço

print(f"O custo para cercar o terreno com tela é de: R$ {custoPerimetro:.2f}")