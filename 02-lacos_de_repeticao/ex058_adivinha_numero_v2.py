# 058
# Melhore o jogo do desafio 28 onde o computador vai pensar num número de 0 a 10.
# Contudo, agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0,10)
acertou = False
cont = 0
print("Vou pensar em um numero entre 0 e 10")
while not acertou:
    jogador = int(input("Escolha o número:"))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(f"Tente novamente mais uma vez, dessa vez com um numero MAIOR")
        else:
            print(f"Tente novamente mais uma vez, dessa vez com um numero MENOR")

print(f"O computador pensou no número {computador}.\n"
      f"PARABÉNS, você acertou com {cont} tentativas\n")