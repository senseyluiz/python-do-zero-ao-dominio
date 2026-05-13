# 109
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais.
# Informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108

from utils.moeda import moeda, metade, dobro, aumentar, diminuir
p = float(input('Digite o preço: '))
print(f"A metade de {moeda(p)} é {moeda(metade(p), True)}")
print(f"O dobro de {moeda(p)} é {moeda(dobro(p), True)}")
print(f"Aumentando 10%, temos {moeda(aumentar(p, 10))}")
print(f"Reduzindo 13%, temos {moeda(diminuir(p, 13))}")