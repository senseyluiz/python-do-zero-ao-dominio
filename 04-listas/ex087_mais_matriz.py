# 87
# Aprimore o exercicio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da Terceira coluna.
# C) O maior valor da Segunda coluna

matriz = [[], [], []]
soma_par = soma_terceira = 0
for i in range(0,3):
    for c in range(0, 3):
        num = int(input(f"Digite um valor para [{i}, {c}]: "))
        if num % 2 == 0:
            soma_par += num
        if c == 2:
            soma_terceira += num
        matriz[i].append(num)
print("-=" * 20)
for valor in matriz:
    for c in range(0, 3):
        print(f"[ {valor[c]} ]", end='')
    print()
print("-=" * 20)
print(f"A soma dos valores pares é {soma_par}\n"
      f"A soma dos valores da terceira coluna é {soma_terceira}\n"
      f"O maior valor da segunda linha é {max(matriz[1])}\n")
