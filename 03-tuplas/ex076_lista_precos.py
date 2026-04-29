# 076
# Crie um programa que tenha uma tupla única com nomes de produtos e os seus respetivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

produtos = ('Caderno', 5, "Caneta", 2, "Régua", 3, "Borracha", 1, "Lápis", 0.50, "Corretivo", 6, 'Pincel', 12, "Estojo", 18, 'Compasso', 32.5)
print("=-" * 25)
print(f'{'LISTA DE PREÇOS':^50}')
print("=-" * 25)

for p in range(len(produtos)):

    if p % 2 == 0:
        print(f'{produtos[p]:.<40} ', end = '')
    else:
        print(f'R${produtos[p]:>7.2f}')
print("=-" * 25)




