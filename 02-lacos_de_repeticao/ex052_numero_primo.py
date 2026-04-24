# 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input("Digite um número: "))
d = 0
primo = "NÃO é PRIMO"
for i in range(1, num + 1):
    if num % i == 0:
        d += 1
        print(f"\033[1;33;48m {i} \033[m", end=" ")
    else:
        print(f"\033[0;32;48m {i} \033[m", end=" ")
if d == 2:
        primo = "É PRIMO"
print(f"\nO número {num} foi divisível {d} vezes\n"
      f"Com isso ele {primo}")

