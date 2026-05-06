# 085
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os numa lista unica que mantenha separados os valores pares e impares
# No final mostre os valores pares e ímpares em ordem crescente.
valores = [[], []]
for i in range(1, 8):
    num = int(input(f"Digite o {i}º valor: "))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()
print("=" * 60)
print(f"Os valores pares digitados foram \33[32m{sorted(valores[0])}\33[m\n"
      f"Os valores impares digitados foram \33[32m{sorted(valores[1])}\33[m")