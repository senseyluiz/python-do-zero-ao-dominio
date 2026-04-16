# 010
# Crie um programa que leia quanto dinheiro tem na carteira e mostre quanros dólares ela pode comprar.
# Considere o dólar a US$1,00 = R$3,7

valor = float(input("Quanto tem na carteira: R$"))
dolar = 3.27
print(f"Com R$ {valor:.2f} você pode comprar US$ {valor / dolar:.2f}")
