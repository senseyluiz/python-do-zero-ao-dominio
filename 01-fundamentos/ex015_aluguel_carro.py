# 015
# Escreva um programa que pergunte a quantidade de Kms percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,015 por km rodado

dias = int(input("Quantos dias alugados: "))
km = int(input("Quantos km rodados: "))
total_pagar = (dias * 60) + (km * 0.15)

print(f"O total a pagar é de R${total_pagar:.2f}")