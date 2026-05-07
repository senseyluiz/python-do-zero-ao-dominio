# 82
# Crie um programa que vai ler vários numeros e colocar numa lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares disgitados respetivamente
# Ao final, mostre o conteúdo das trê listas

valores = list()
while True:
    num = int(input("Digite um valor: "))
    valores.append(num)
    continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while True:
        if continuar not in "SN":
            print("Opção invalida. Tente novamente.")
            continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
        else:
            break
    if continuar == "N":
        break

pares= list()
impares= list()
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print("-=" * 30)
print(f"Os valores digitados foram {valores}\n"
      f"Os valores pares são {pares}\n"
      f"Os valores impares são {impares}")