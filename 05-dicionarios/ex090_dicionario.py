# 090
# Faça um programa que leia nome e média de um aluno, guardando também a situação num dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = {}
aluno = str(input("Nome do aluno: ")).strip()
media = float(input("Media do aluno: "))
boletim["Nome"] = aluno
boletim["Media"] = media
if media >= 7:
    boletim["Situacao"] = "Aprovado"
else:
    boletim["Situacao"] = "Reprovado"
print(f"Nome do aluno: {aluno}\n"
      f"Media do aluno: {media}")
print(f"Situação do aluno: {boletim['Situacao']}")