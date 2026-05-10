# 098
# Faça um program que tenha uma função chamada contador(), que recebe três parâmetros: inicio, fim e passo e realize a contagem.
# O seu programa tem que realizar três contagens através da função criada:
# A) De 1 até dez, de 1 em 1
# B) De 10 até 0, de 2 em 2
# Uma contagem personalizada
from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    passo = abs(passo)
    print('-=' * 20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if inicio > fim:
        for c in range(inicio, fim - 1, - passo):
            sleep(0.5)
            print(c, end=" ")
    else:
        for c in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(c, end=" ")

    print("FIM!")

contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)