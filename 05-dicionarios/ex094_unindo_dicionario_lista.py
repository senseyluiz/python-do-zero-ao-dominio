# 094
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa num dicionário e todos os dicionários numa lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados= []
while True:
    pessoa = {'nome': str(input('Nome: '))}
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo not in 'MF':
            print("ERRO! Por favor, digite apenas M ou F")
        else:
            pessoa['sexo'] = sexo
            break
    pessoa['idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in "SN":
            break
        print("ERRO! Por favor, digite apenas S ou N")
    if resp == 'N':
        break
idades = []
for i, v in enumerate(dados):
    idades.append(v['idade'])
media = sum(idades) / len(idades)
print("-=" * 40)
print(dados)
print(f"A) Ao todo, temos {len(dados)} pessoas cadastradas.\n"
      f"B) A média de idade é de {media:.2f} anos.")
print("C) As mulheres cadastradas foram ", end='')
for i, v in enumerate(dados):
    if v['sexo'] == 'F':
        print(f" {v['nome']} ", end='')
print("\nD) Lista das pessoas que estão acima da média:")
for i, v in enumerate(dados):
    if v['idade'] > media:
        print(f"Nome =  {v['nome']}; Sexo = {v['sexo']}; Idade = {v['idade']}")
print(f"{' ENCERRADO ':=^60}")