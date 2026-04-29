# 041
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria de cordo com a idade:
# Até 9 anos:-MIRIM
# Até 14 anos: -INFANTIL
# Até 19 anos: -Júnior
# Até 25 anos: -SÊNIOR
# Acima de 25 anos: -MASTER
from datetime import date
ano = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano
if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JUNIOR"
elif idade <= 25:
    categoria = "SENIOR"
else:
    categoria = "MASTER"

print(f"O atleta tem {idade} anos.\n"
      f"Sua categoria: {categoria}")