# 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = input("Digite o nome da cidade: ").strip()
santo = cidade.split()[0].lower() == "santo"

print(f"Cidade: {cidade}\n"
      f"Começa com 'Santo': {santo}\n")