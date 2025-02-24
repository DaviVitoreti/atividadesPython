tempoGasto = float(input("Digite o tempo gasto, em horas, da viagem: "))
velocidadeMedia = int(input("Digite a velocidade média, em km/h, da viagem: "))

distancia = velocidadeMedia * tempoGasto
consumo = distancia / 12

print(f"\n\t Velocidade média: {velocidadeMedia} km/h")
print(f"\t Tempo gasto: {tempoGasto} horas")
print(f"\t Distância percorrida: {distancia} km")
print(f"\n\t Combustível consumido: {consumo} litros")