# 070
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual o total gasto na compra
# B) Quantos produtos custa mais de R$1000
# C) Qual é o nome do produto mais barato

print("==== LOJÃO DO COMÉRCIO ====")

total_gasto = count_mais_caro = mais_barato = cont =  0
nome_barato = ""

while True:
    produto = str(input("Nome do produto: ")).strip()
    PRECO = float(input("Preço: R$"))
    total_gasto += PRECO
    cont += 1
    if PRECO > 1000:
        count_mais_caro += 1
    if cont == 1:
        mais_barato = PRECO
        nome_barato = produto
    if mais_barato > PRECO:
        mais_barato = PRECO
        nome_barato = produto
    continua = " "
    while continua not in "SN":
        continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continua == "N":
        break

print("==== FIM DO PROGRAMA ====")
print(f"Total da compra: R${total_gasto:.2f}\n"
      f"Quantidade de produtos com valor acima de R$1000,00: {count_mais_caro:.2f}\n"
      f"Produto mais barato foi {nome_barato}: {mais_barato:.2f}\n")
