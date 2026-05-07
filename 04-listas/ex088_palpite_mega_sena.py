# 088
# Faça um programa que ajude o jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo numa lista composta
from random import randint
from time import sleep
print("-=" * 30)
print(f"{'JOGA NA MEGA SENA':^60}")
print("-=" * 30)
qtd = int(input('Quantos jogos você quer que eu sorteie: '))
jogos = [[] for c in range(0, qtd)]

for c in range(0, qtd):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos[c]:
            jogos[c].append(num)
            cont += 1
        if cont == 6:
            break
    jogos[c].sort()
print("--" * 30)
print(f"{f'\33[32mSorteando {qtd} Jogos':^60}\33[m")
print("--" * 30)
for i, v in enumerate(jogos):
    sleep(1)
    if i % 2 == 0:
        print(f"Jogo {i+1}: \33[34m{v}\33[m")
    else:
        print(f"Jogo {i + 1}: \33[35m{v}\33[m")

print(f"\33[33m{' < BOA SORTE > ':*^60}\33[m")