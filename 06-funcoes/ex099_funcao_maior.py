# 99
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# O seu programa tem que analizar todos os valores e dizer qual deles é maior

def maior(*num):
    maior = 0
    print('-=' * 30)
    print("Analizando os valores passados ... ")
    for n in range(0, len(num)):
        if n == 0:
            maior = num[n]
        else:
            if num[n] > maior:
                maior = num[n]
        print(num[n], end=" ")
    print(f"Foram informados {len(num)} valores ao todo.\n"
          f"O maior valor informado foi {maior}.")


maior(5,3,8,4,2)
maior(6)
maior()


