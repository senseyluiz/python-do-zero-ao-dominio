# 096
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área o terreno

def area(lar, comp):
    area = lar * comp
    print(f'A área de um terreno {lar:.1f} x {comp:.1f} é de {area:.1f}m²')

print(f'{"CONTROLE DE TERRENO":^40}')
print('-' * 40)
larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))

area(larg, comp)