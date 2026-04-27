# 065
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = True
maior = 0
menor = 9999999999999
soma = 0
cont = 0

while continuar:
    num = int(input("Digite um numero: "))
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        continuar = False

media = soma / cont
print(f"Você digitou {cont} números e a media entre eles foi de {media}\n"
      f"O maior valor digitado foi de {maior} e o menor foi de {menor}")