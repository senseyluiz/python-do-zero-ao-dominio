# 022
# Crie um programa que leia o nome de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras tem ao todo sem considerar espaços
# Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ").strip()
print(f"Nome em maiúsculo: {nome.upper()}\n"
      f"Nome em minúsculo: {nome.lower()}\n"
      f"Quantidade de letras sem espaços: {len(nome) - nome.count(' ')}\n"
      f"Quantidade de letras primeiro nome: {len(nome.split()[0])}\n")
