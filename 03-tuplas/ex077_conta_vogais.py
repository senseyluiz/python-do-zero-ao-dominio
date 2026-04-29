# 077
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('carro', 'caneta', 'bicicleta', 'coroa', 'mulher', 'geringonça', 'motocicleta')
for palavra in palavras:
    print(f'Na palavra \33[34m{palavra}\33[m temos as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'\33[32m{letra.lower()}\33[m', end= " ")

    print()