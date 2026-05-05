# 078
# Faça um programa que leia 5 valores e guarde-os numa lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respetivas posições

valores = list()
for c in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {c}: ")))

print(f"Você digitou os valores {valores}\n"
      f"O maior valor digitado foi {max(valores)} que está nas posições ", end="" )
for i, v in enumerate(valores):
    if v == max(valores):
        print(i, end="...")

print(f"\nO menor valor digitado foi {min(valores)} que está nas posições ", end="" )

for i, v in enumerate(valores):
    if v == min(valores):
        print(i, end="...")