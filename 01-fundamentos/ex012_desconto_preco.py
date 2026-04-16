# 012
# Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto

preco = float(input("Digite o preço do produto: "))
preco_com_desconto = preco * 0.95
print(f"Para o produto com preço de R${preco:.2f} com desconto de 5%, o valor será de R${preco_com_desconto:.2f}")