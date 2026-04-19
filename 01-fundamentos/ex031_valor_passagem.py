# 31
# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 por viagens mais longas.
distancia = int(input("Digite a distancia da viagem: "))
valor = 0
if distancia > 200:
    valor = distancia * 0.45
else:
    valor = distancia * 0.50

print(f"Distancia da viagem: {distancia}km\n"
      f"O valor a ser pago em R${valor:.2f}")