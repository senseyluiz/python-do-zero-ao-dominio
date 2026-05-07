# 091
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados num dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
ranking = list()
for i in range(1,5):
    jogador[f'Jogador{i}'] = randint(1, 6)
print("Valores Sorteados: ")
for k, v in jogador.items():
    sleep(1)
    print(f" O jogador {k} tirou {v}")
print("-" * 30)
print("\33[32mRanking dos jogadores\33[m")
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f"{i+1}º colocado: {v[0]} com {v[1]}")





