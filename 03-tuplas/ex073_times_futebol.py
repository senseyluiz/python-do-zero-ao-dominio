# 073
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da Chapecoense

tabela = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Coríntihans', 'Ponte Preta', 'Grêmio', 'São Paulo', 'Chapecoense', 'Fluminense', 'Cruzeiro', 'Sport', 'Curitiba', 'Vitória', 'Internacional (R)', 'Figueirense', 'Santa Cruz', 'América-MG')

print(f'=-' * 15)
print(f'{"Tabela Brasileirão 2016":^30}' )
print(f'=-' * 15)
print()

for pos, time in enumerate(tabela):
    print(f'{pos + 1}º - {time}')

print('=-' * 45)
print(f'\033[32mOs 5 primeiros são:\033[m {tabela[:5]}')
print('=-' * 45)
print(f'\033[32mOs 4 últimos são:\033[m {tabela[16:20]}')
print('=-' * 45)
print(f'\033[32mTimes em ordem alfabética:\33[m {sorted(tabela)}')
print('=-' * 45)
print(f'\033[32mO Chapecoense está na {tabela.index("Chapecoense") + 1 }ª posição\33[m')

