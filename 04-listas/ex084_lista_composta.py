# 084
# Faça um programa que leia nomes e peso de várias pessoas, guardando tudo numa lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves
alunos = list()
aluno = list()

while True:
    nome = str(input("Digite o nome do aluno: "))
    peso = float(input("Digite o peso do aluno: "))
    aluno.append(nome)
    aluno.append(peso)
    alunos.append(aluno[:])
    aluno.clear()
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if resp in 'N':
        break
mai = men = alunos[0][1]
mais_pesados = list()
menos_pesados = list()
for c in alunos:
    if c[1] > mai:
        mai = c[1]
    if c[1] < men:
        men = c[1]

for c in alunos:
    if c[1] == mai:
        mais_pesados.append(c[0])
    if c[1] == men:
        menos_pesados.append(c[0])


print(f"Ao todo foram cadastrados {len(alunos)} alunos.\n"
      f"O maior peso foi  {mai} que pertence a {mais_pesados}\n"
      f"O menor peso foi {men} que pertence a {menos_pesados}\n")