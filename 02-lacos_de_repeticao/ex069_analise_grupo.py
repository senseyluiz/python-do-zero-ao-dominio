# 069
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos

print("=-" * 13)
print("CADASTRO DE IDADES E SEXO")
print("=-" * 13)
total18 = homens = mulheres20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo= str(input("Sexo: [M/F] ")).strip().upper()[0]
    continua = ' '
    while continua not in "SN":
        continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    print("-" * 30)
    if idade >= 18:
        total18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 15:
        mulheres20 += 1
    if continua == "N":
        break

print("==== FIM DO PROGRAMA ====")
print(f"Total de pessoas maiores de 18 anos: {total18}\n"
      f"Total de homens cadastrados: {homens}\n"
      f"Total de mulheres com menos de 18 anos: {mulheres20}\n")

