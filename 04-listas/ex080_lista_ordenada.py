# 080
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os numa lista, já na posição correta de inserção(sem usar o sort().
# No final, mostre a lista ordenada na tela.

valores = list()
for c in range(0, 5):
    num = int(input("Digite um valor: "))
    if len(valores) == 0 or num >= max(valores):
        valores.append(num)
        print("Adicionado no final da lista")
    else:
        pos = 0
        while pos < len(valores):
            if num < valores[pos]:
                valores.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista")
                break
            pos += 1

print(valores)