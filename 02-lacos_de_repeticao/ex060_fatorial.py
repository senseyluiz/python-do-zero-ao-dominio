# 060
# Faça um programa que leia um número qualquer e mostre o seu fatorial
num = int(input("Digite um numero para ver seu fatorial: "))
total = 1
print(f"{num}! = ", end="")
while num != 0:
    if num == 1:
        print(num, end="=")
    else:
        print(num, end='x')
    total *= num
    num -=1
print(total)