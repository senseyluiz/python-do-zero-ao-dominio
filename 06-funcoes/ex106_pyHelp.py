# 106
# Faça um mini-sistema que utilize o interactive help do python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palávra "FIM", o programa encerrará.
# OBS: use cores

c = [
    '\033[m',           # 0 - sem cores
    '\033[0;30;41m',    # 1 - vermelho
    '\033[0;30;42m',    # 2 - verde
    '\033[0;30;43m',    # 3 - amarelo
    '\033[0;30;44m',    # 4 - azul
    '\033[0;30;45m',    # 5 roxo
    '\033[7;30m'        # 6 branco
]

def pyHelp(aj):
    titulo(f"Acessando o manual do comando \"{aj}\"", 4)
    print(c[3])
    help(aj)
    print(c[0])

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print('=' * tam)
    print(f'  {msg}  ')
    print('=' * tam)
    print(c[0])


while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    ajuda = str(input("Função ou Biblioteca > "))
    if ajuda.upper() == "FIM":
        break
    else:
        pyHelp(ajuda)
titulo("Até Logo", 1)