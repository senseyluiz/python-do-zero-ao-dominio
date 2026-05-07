time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

# --- EXIBIÇÃO DOS RESULTADOS ---
print('-=' * 30)
print(f'{"cod":<4} {"nome":<15} {"gols":<18} {"total":<5}')
print('-' * 50)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    # Aqui formatamos para garantir que a lista de gols não quebre o layout
    print(f'{v["nome"]:<15} {str(v["gols"]):<18} {v["total"]:<5}')
print('-' * 50)

# --- SISTEMA DE DETALHES ---
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)

print('<< VOLTE SEMPRE >>')