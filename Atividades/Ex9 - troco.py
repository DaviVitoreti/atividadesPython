valorCompra = int(input("Digite o valor da compra: "))
valorPago = int(input("Digite o valor pago pelo cliente: "))

troco1 = valorPago - valorCompra
cedulas100 = troco1 // 100
troco2 = troco1 - 100 * cedulas100
cedulas50 = troco2 // 50
troco3 = troco2 - 100 * cedulas50
cedulas20 = troco3 // 20
troco4 = troco3 - 100 * cedulas20
cedulas10 = troco4 // 10
troco5 = troco4 - 100 * cedulas10
cedulas5 = troco5 // 5
troco6 = troco5 - 100 * cedulas5
cedulas1 = troco6

print(troco1)
print(troco2)
print(troco3)
print(troco4)
print(troco5)
print(troco6)
print("R$100,00 ", cedulas100, " cédulas")
print("R$50,00 ", cedulas50, " cédulas")
print("R$20,00 ", cedulas20, " cédulas")
print("R$10,00 ", cedulas10, " cédulas")
print("R$5,00 ", cedulas50, " cédulas")
print("R$1,00 ", cedulas1, " cédulas")