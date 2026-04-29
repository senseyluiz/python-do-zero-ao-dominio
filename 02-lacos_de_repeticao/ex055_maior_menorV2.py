# 055
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o meno peso lidos.
maior = 0
pesos = []
for i in range(0,5):
    peso = float(input(f"Digite o {i +1}º peso: "))
    pesos.append(peso)

print(f"O maior peso digitado foi: {max(pesos):.2f} e o menor foi: {min(pesos):.2f}")