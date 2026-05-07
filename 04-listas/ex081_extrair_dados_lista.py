# 081
# Crie um programa que vai ler vários números e colocar numa lista.
# Depois mostre:
# A) Quantos números foram digitados.
# B) A lista de valores ordenadas de for decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
valores = list()
while True:
    num = int(input("Digite um valor: "))
    valores.append(num)
    continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while True:
        if continuar not in 'NS':
            print("Opção invalida. Tente novamente.")
            continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
        else:
            break
    if continuar == 'N':
        break

print("-=" * 30)
print(f"Você digitou {len(valores)} elementos\n"
      f"Os valores em ordem decrescente são {sorted(valores, reverse=True)}\n"
      f"O valor 5 ", end='')
if 5 in valores:
    print('\33[32mfaz parte da lista\33[m5')
else:
    print('\33[31mnão faz parte da lista\33[m')