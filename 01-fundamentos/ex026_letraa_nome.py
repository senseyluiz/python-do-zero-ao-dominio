# 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
## Em que posição ela aparece a última vez

frase = input("Digite uma frase: ").strip()
print(f"{frase}\n"
      f"A letra 'a' aparece quantas vezes: {frase.lower().count('a')}\n"
      f"Em que posição ela aparece a primeira vez: {frase.lower().find('a') + 1}\n"
      f"Em que posição ela aparece a última vez: {frase.lower().rfind('a') + 1}\n")