# 34
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00 calcule o aumento de 10%
# Para salários inferiores ou iguais, calcule o aumento de 15%
salario = float(input("Salário  do funcionário: R$"))
salario_novo = salario
if salario > 1250.00:
    salario_novo = salario * 1.10
if salario <= 1250.00:
    salario_novo = salario * 1.15
print(f"Salário atual: R${salario:.2f}\n"
      f"Salário novo: R${salario_novo:.2f}\n")