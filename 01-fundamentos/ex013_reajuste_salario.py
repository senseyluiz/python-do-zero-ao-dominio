# 013
# Faça um algoritimo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento

salario = float(input("Digite seu salário: "))
salario_com_aumento = salario * 1.15
print(f"Seu salário é de R${salario:.2f} e com 15% {salario_com_aumento:.2f}")
