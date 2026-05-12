# 108
# Adapte o código do exercicio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetario
from utils.moeda import moeda, metade, dobro, aumentar, diminuir
p = float(input('Digite o preço: '))
print(f"A metade de {moeda(p)} é {moeda(metade(p))}")
print(f"O dobro de {moeda(p)} é {moeda(dobro(p))}")
print(f"Aumentando 10%, temos {moeda(aumentar(p, 10))}")
print(f"Reduzindo 13%, temos {moeda(diminuir(p, 13))}")