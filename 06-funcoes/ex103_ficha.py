# 103
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome do jogador e quantos "gols" ele marcou.
# O programa deverá ser capaz de mostrar a ficha fo jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador = "desconhecido", gols = 0):
    return f"O jogador {jogador} fez {gols} gols no campeonato."

jog = str(input("Nome do Jogador: ")).strip()
gols = str(input("Número de GOLS: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jog == "":
    print(ficha(gols= gols))
else:
    print(ficha(jog, gols))