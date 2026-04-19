# 33
# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = int(input("Digite outro número inteiro: "))
maior = num1
menor = num1

# Verifica maior
if num2 > num1:
    maior = num2
if num3 > num2:
    maior = num3

# Verifica menor
if num1 < num2:
    menor = num1
if num3 < num2:
    menor = num3


print (f"O maior número é {maior}")
print (f"O menor número é {menor}")