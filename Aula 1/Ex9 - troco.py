valorCompra = int(input("Digite o valor da compra: "))
valorPago = int(input("Digite o valor pago pelo cliente: "))
troco = valorPago - valorCompra

n100 = troco // 100
troco = troco % 100
n50 = troco // 50
troco = troco % 50
n20 = troco // 20
troco = troco % 20
n10 = troco // 10
troco = troco % 10
n5 = troco // 5
troco = troco % 5

print(f"\n\t Valor pago: R${valorPago:.2f}")
print(f"\n\t Valor da compra: R${valorCompra:.2f}")
print(f"\n\t R${valorCompra - valorPago:.2f}")
print(f"\n\t Sendo:\n")
print(f"\n\t\t Notas de R$100: {n100}")
print(f"\n\t\t Notas de R$50: {n50}")
print(f"\n\t\t Notas de R$20: {n20}")
print(f"\n\t\t Notas de R$10: {n10}")
print(f"\n\t\t Notas de R$5: {n5}")
print(f"\n\t\t Notas de R$1: {troco}")