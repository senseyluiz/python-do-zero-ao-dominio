# 040
# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem mo final com a média atingida
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

print(f"Com as notas {nota1:.1f} e {nota2:.1f} tem a média de: {media:.1f}")
result = "APROVADO"
if media >= 7:
    result = "APROVADO"
elif media < 5:
    result = "REPROVADO"
else:
    result = "RECUPERAÇÃO"

print(f"O Aluno foi {result}")