# 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre a mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = int(input("Digite a velocidade do veículo: "))
multa = 0
if velocidade > 80:
    acima = velocidade - 80
    multa = (velocidade - 80) * 7
    print(f"Você ultrapassou o limite de velocidade em {acima}Km/h")
    print(f"Você foi multado em R${multa:.2f}")
else:
    print("Dentro do limite de velocidade.")