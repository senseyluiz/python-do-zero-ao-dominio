# 032
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = str(input("Digite o ano: ")).strip()
print(f"O ano escolhido foi: {ano}")
if int(ano[2:4]) != 00:
    if int(ano[2:4]) % 4 == 0:
        print("Ano Bissexto")
else:
    print("Ano não é Bissexto")
