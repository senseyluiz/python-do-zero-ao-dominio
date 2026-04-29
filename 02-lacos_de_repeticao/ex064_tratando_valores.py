# 064
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai para quando o usuário digitar 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles. (Desconsiderando a flag)

resp = True
cont = 0
soma = 0
while resp:
    num = int(input("Digite um numero (999 para sair): "))
    if num == 999:
        resp = False
    else:
        cont += 1
        soma += num
print(f"Você digitou {cont} números e a soma entre eles foi de {soma}")