# 92
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) num dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano da contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
idade = datetime.now().year - nasc
dados['Idade'] = idade
dados['CTPS'] = int(input('CTPS: (0 não tem) '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados["Salario"] = float(input('Salario: R$ '))
    dados['Aposentadoria'] = ((dados['Contratação'] + 35) - datetime.now().year) + dados['Idade']

print("-"*30)
for k, v in dados.items():
    print(f"{k} tem o valor: {v} ")
