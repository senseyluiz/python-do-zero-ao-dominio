# 072
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 a vinte.
# O seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    usuario = int(input('Digite um número entre 0 e 20: '))
    while usuario < 0 or usuario > 20:
        usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[usuario]}')
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
