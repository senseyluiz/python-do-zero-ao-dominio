# 016
# Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira.
import math
num = float(input("Digite um número: "))
print(f"O número {num} tem a parte inteira {math.trunc(num)}")