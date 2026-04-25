# 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tintaNecessaria = area / 2

print(f"Para uma parede de {largura:.2f}m largura e {altura:.2f}m de altura temos uma área de {area:.2f}m².\n"
      f"Será necessário {tintaNecessaria:.2f}Lts de tinta para pintá-la" )