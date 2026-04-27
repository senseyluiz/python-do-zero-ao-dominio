# 062
# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais algums termos.
# O programa encerra quando ele disser que quer mostrar "0" termos.

print("==" * 15)
print(f"{" 10 TERMOS DE UMA PA ":=^30}")
print("==" * 15)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
mais_termos = 10
total = 0
cont = 0
while mais_termos != 0:
    total += mais_termos
    while cont < total:
        if cont == total:
            print(termo)
        else:
            print(f"{termo} -> ", end="")
            termo += razao
            cont += 1
    print("pausa")
    mais_termos = int(input("\nQuer mostrar mais quantos termos: "))
print("FIM")

