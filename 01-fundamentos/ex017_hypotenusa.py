# 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
import math
ca = float(input("Digite o valor do cateto adjacente: "))
co = float(input("Digite o valor do cateto oposto: "))
hip = math.hypot(ca, co)
print(f"Com cateto adjacente de {ca}  e cateto oposto de {co}, a hipotenusa é:  {hip:.2f}")