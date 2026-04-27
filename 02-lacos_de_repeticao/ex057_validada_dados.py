# 57
# Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores "V" ou "F".
# Caso esteja errado, peça a digitação novamente até ter o valor correto.

sexo = input("Qual seu sexo: [M/F] ").upper().strip()
while sexo not in ("M", "F"):
    print("Sexo invalido, Tente novamente")
    sexo = input("Qual seu sexo: [M/F] ").upper().strip()
print(f"O sexo digitado foi: {"Masculino" if sexo == "M" else "Feminino" }")
