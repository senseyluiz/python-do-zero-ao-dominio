# 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input("Digite seu nome completo: ").strip()
print(f"Tem 'Silva' no nome: {'silva' in nome.lower()}\n")