# 079
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()
while True:
    num = int(input("Digite um valor: "))
    if num in valores:
        print("Valor duplicado. Tente novamente.")
        continue
    valores.append(num)
    continuar = input("Deseja continuar? [S/N] ").upper().strip()[0]
    while True:
        if continuar not in "SN":
            print("Valor invalido. Tente novamente.")
            continuar = input("Deseja continuar? [S/N] ").upper().strip()[0]
        else:
            break
    if continuar == "N":
       break

valores.sort()
print(f"Você digitou os valores {valores}")

