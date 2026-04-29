# 074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint
a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)
e = randint(1, 10)
nuns = (a, b, c, d, e)

print("Os números sorteados foram: ", end = '')
for n in nuns:
    print(n, end = ' ')

print(f'\nO maior valor sorteado foi {max(nuns)}\n'
      f'O menor valor sorteado foi {min(nuns)}')
