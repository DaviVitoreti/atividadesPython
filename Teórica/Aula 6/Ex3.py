texto = input("Digite uma frase: ")
texto_menor = texto.lower()

texto=texto_menor.replace("a","")
texto=texto_menor.replace("e","")
texto=texto_menor.replace("i","")
texto=texto_menor.replace("o","")
texto=texto_menor.replace("u","")

print(f"{texto}")