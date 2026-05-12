
#%%
# 101
# Crie um programa que tenha uma função  chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    if 16 <= idade < 18 or idade >= 65:
        voto = "VOTO OPCIONAL"
    elif idade >= 18:
        voto = "VOTO OBRIGATÓRIO"
    else:
        voto = "VOTO NEGADO"
    return f"Com {idade} anos: {voto}"


ano = int(input("Informe o ano de nascimento: "))
print(voto(ano))

