# 059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# O programa deverá realizar a operação solicitada em cada conta
from time import sleep
valor1 = int(input("Digite o 1º valor: "))
valor2 = int(input("Digite o 2º valor: "))
sair = True

print("=-=" * 10)
print("[1] Somar\n"
    "[2] Multiplicar\n"
    "[3] Maior\n"
    "[4] Novos números\n"
    "[5] Sair do programa")
print("=-=" * 10)

while sair:
    sleep(1)
    print("=-=" * 10)
    print("[1] Somar\n"
        "[2] Multiplicar\n"
        "[3] Maior\n"
        "[4] Novos números\n"
        "[5] Sair do programa")
    print("=-=" * 10)
    opcao= int(input("Escolha sua opção: "))
    if opcao == 1:
        soma = valor1 + valor2
        print(f"A soma de {valor1} e {valor2} é {soma}")
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print(f"A multiplicação de {valor1} e {valor2} é {multiplicar}")
    elif opcao == 3:
        print(f"O maior valor entre {valor1} e {valor2} é {max(valor1, valor2)}")
    elif opcao == 4:
        print("Digite novos valores: ")
        valor1 = int(input("Digite o 1º valor: "))
        valor2 = int(input("Digite o 2º valor: "))
    elif opcao == 5:
        print("Saindo do programa")
        sair = False
    else:
        print("Opção incorreta, tente novamente")
