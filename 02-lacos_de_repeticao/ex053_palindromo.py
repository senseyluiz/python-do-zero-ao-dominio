# 053
# Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços

frase = input("Digite uma frase: ").strip()
frase_form = frase.replace(" ", "").lower().replace("-", "").replace(",", "")
frase_inversa =""
for i in range(len(frase_form), 0, -1):
    frase_inversa += frase_form[i-1]

print(f"O inverso de {frase} é {frase_inversa}")
if frase_form == frase_inversa:
    print(f"A frase '{frase}' é um PALINDROMO")
else:
    print(f"A frase '{frase}' NÃO é um PALINDROMO")