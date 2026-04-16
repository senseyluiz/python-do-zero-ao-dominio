# 008
# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

medida=float(input("digite um valor: "))

cent = medida * 100
mili = medida * 1000

print(f"O valor de {medida} metros convertido para centímetros é {cent:.2f}\n"
      f"O valor de {medida} metros convertido para milímetros é {mili:.2f}")