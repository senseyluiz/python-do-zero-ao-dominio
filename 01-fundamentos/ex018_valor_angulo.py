# 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = float(input("Digite um ângulo qualquer: "))
print(f"O seno do ângulo {ang} é {sin(radians(ang)):.2f}\n"
      f"O cosseno do ângulo {ang} é {cos(radians(ang)):.2f}\n"
      f"A tangente do ângulo {ang} é {tan(radians(ang)):.2f}\n")
