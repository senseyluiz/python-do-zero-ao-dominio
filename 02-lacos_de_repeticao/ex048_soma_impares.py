# 048
# Faça um programa que calcule a soma entre todos os números ímpares múltiplos de 3 e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for i in range(1, 500):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
        cont += 1
print(f"A Soma dos {cont} números entre 1 e 500 ímpares múltiplos de 3 é: {soma}")