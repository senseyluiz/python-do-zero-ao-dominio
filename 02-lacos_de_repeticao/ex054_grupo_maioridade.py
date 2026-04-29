# 054
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já estão maiores.
from datetime import date
maior = 0
menor = 0
digitados = []
for i in range(0, 7):
    ano_pessoa = int(input(f"Digite o {1 + i}º ano de nascimento: "))
    idade = date.today().year - ano_pessoa
    digitados.append(idade)
    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f"Para os anos que você digitou tem idades de {digitados}, {menor} pessoas são menores e  {maior} pessoas são maiores.")
