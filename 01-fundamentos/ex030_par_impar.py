# 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR oou IMPAR

num = int(input("Digite um número inteiro: "))
print(f"O número escolhido foi : {num}")
if num % 2 == 0:
    print("Este número é PAR")
else:
    print("Este número é IMPAR")