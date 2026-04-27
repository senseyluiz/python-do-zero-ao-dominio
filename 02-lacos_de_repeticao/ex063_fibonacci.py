# 063
# Escreva um programa que leia um número 'n' inteiro qualquer e
# mostre na tela os 'n' primeiros elementos da sua sequência de Fibonacci

num = int(input("Digite um numero: "))
t1 = 0
t2 = 1
t3 = t1 + t2
count = 0

while count < num:
    if count == num - 1:
        print(f"{t1}")
    else:
        print(f"{t1} -> ", end="")
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    count += 1

