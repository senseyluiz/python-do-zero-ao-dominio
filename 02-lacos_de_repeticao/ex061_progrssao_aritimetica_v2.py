# 061
# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while
print("==" * 15)
print(f"{" 10 TERMOS DE UMA PA ":=^30}")
print("==" * 15)
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
cont = 0
while cont < 10:
    print(f"{termo} -> ", end="")
    termo += razao
    cont += 1
print("FIM")