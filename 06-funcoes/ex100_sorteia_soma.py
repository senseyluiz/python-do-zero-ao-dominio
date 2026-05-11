# 100
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
def sorteia(lista):
    for i in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"\nSomando os valores pares de {lista}, temos {soma}")


numeros = []
sorteia(numeros)
print('Sorteando 5 valores da lista: ', end="")
for num in numeros:
    print(num, end=" ")
somaPar(numeros)



