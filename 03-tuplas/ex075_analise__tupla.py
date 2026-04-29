# 075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o valor 3
# C) Quais foram os números pares

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite um último número: '))
nuns = (a, b, c, d)
print(f'Você digitou os valores: {nuns}')
print(f'o valor 9 apareceu na {nuns.count(9)} vezes')
if 3 in nuns:
    print(f'O valor 3 apareceu na posição {nuns.index(3) + 1 }')

else:
    print(f'O valor 3 não apareceu em nenhuma posição.')

print(f'O valores pares digitados são: ', end = " ")
for n in nuns:
    if n % 2 == 0:
        print(n, end = ' ')
