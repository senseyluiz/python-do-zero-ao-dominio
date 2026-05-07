# 89
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta.
# No final, mostre o boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = []
while True:
    nome = str(input("Nome: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resp = input("Quer continuar? [S/N] ").strip().upper()[0]
    if resp in "Nn":
        break
print("-="*30)
print(f"{'Nº':<4}{'Nome':<10}{'MÉDIA':>8}")
print("_"*26)
for i, v in enumerate(boletim):
    print(f"{i:<4}{v[0]:<10}{v[2]:>8.1f}")

while True:
    print("-="*30)
    nota = int(input("Quer ver a nota de qual aluno?  (999 interrompe) "))
    if nota == 999:
        break
    if nota <= len(boletim):
        print(f"Notas de {boletim[nota][0]} são {boletim[nota][1]}")

