# 014
# Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para Fahrenheit

celsius = float(input("Digite o valor da temperatura em °C: "))
f = celsius * 1.8 + 32

print(f"A temperatura de {celsius}°C corresponde a {f:.1f}°F")