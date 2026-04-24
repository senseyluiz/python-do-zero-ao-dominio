# 045
# Exercício Python 45:
from random import choice
from time import sleep
print ("==== JOKENPÔ ====\n"
       "Sua opção:\n"
       "[0] PEDRA\n"
       "[1] PAPEL\n"
       "[2] TESOURA\n")
opcao = int(input("Qual é sua jogada: "))
computador = choice(("PEDRA", "PAPEL", "TESOURA"))
if opcao == 0:
    jogador = "PEDRA"
elif opcao == 1:
    jogador = "PAPEL"
elif opcao == 2:
    jogador = "TESOURA"
else:
    print("OPÇÃO INCORRETA. Tente novamente.")

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")

print("-=" * 13)
print(f"Computador jogou {computador}.\n"
      f"Jogador jogou {jogador}.")
print("-=" * 13)


if computador == jogador:
    print(f"EMPATE.")
elif computador == "PEDRA" and jogador == "PAPEL":
    print("Jogador VENCEU!")
elif computador == "PEDRA" and jogador == "TESOURA":
    print("Computador VENCEU!")
elif computador == "PAPEL" and jogador == "PEDRA":
    print("Computador VENCEU!")
elif computador == "PAPEL" and jogador == "TESOURA":
    print("Jogador VENCEU!")
elif computador == "TESOURA" and jogador == "PEDRA":
    print("Jogador VENCEU!")
elif computador == "TESOURA" and jogador == "PAPEL":
    print("Computador VENCEU!")
else:
    print("SEM VENDEDOR")