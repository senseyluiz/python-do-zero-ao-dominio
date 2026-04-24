# 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print("==" * 15)
print(f"{" 10 TERMOS DE UMA PA ":=^30}")
print("==" * 15)
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
for i in range(0, 10):
    print(f"{termo} -> ", end="")
    termo += razao
print("FIM")