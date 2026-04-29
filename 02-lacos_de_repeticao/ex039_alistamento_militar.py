# 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele vai se alistar ao serviço milita,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}")

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.\n"
          f"Seu alistamento será em {ano_atual + 18 -idade}")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.\n"
          f"Seu alistamento foi em {ano_atual -  idade + 18}")
else:
    print(f"Você tem que se alistar IMEDIATAMENTO.")

