# 068
# Faça um programa que jogue par ou impar com o computador.
# O jogo sé será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
print("=-" * 15)
print("JOGO PAR OU IMPAR" )
print("=-" * 15)
while True:
    numPc = randint(0, 10)
    num_jogador = int(input("Digite um valor: "))
    escolha = input("Par ou Ímpar? [P/I] ").strip().upper()[0]
    print("-" * 30)
    soma = numPc + num_jogador
    result = "PAR" if soma % 2 == 0 else "IMPAR"
    print(f"Você jogou {num_jogador} e o computador jogou {numPc}.\n"
          f"Total deu {soma}. DEU {result}   ")
    if result[0] == escolha:
        print("Você VENCEU!!!\n"
              "Vamos Jogar novamente.")
        cont += 1
    else:
        print("Você PERDEU!!!")
        break
print(f"\nGAME OVER! Você venceu {cont} vezes")

