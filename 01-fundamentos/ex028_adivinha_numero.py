# 028
# Escreva um programa que faça o computador pensar num número entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deve escrever na tela se o usuário venceu ou perdeu

import random
from time import sleep
comp = random.randint(0, 5)
user = int(input("Escolha um número entre 0 e 5: "))
print("Processando...")
sleep(2)
print(f"O número escolhido pelo computador foi: {comp}")
sleep(0.5)
print(f"O número que você escolheu foi: {user}")
sleep(0.5)
if user == comp:
    print("Você acertou! PARABÉNS")
else:
    print("Infelizmente você errou.")
