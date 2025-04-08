texto = input("Escreva uma frase de no máximo 20 caracteres: ")
cont = 0

while (len(texto) > 20):
    texto = input("Por favor, digite uma frase de no máximo 20 caracteres: ")

for index in range(len(texto)):
    if (texto[index]=="a"):
        cont += 1

if (cont == 0):
    print(f"Não existem letras \"a\" na frase")
else:
    print(f"A frase contém {cont} letras \"a\".")