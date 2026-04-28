# 066
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa vai parar quando o usuário digitar 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando a flag)

cont = soma = 0
while True:
    num = int(input("Digite um numero (999 para sair): "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"A soma dos {cont} números foi {soma}")