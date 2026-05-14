# 113
# Reescreva a função leiaInt() do desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg=""):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\33[31mERRO! Digite um número inteiro válido\33[m")
        else:
            break
    return int(n)

def leiaFloat(msg=""):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\33[31mERRO! Digite um número real válido\33[m")
        else:
            break
    return float(n)

n = leiaInt("Digite um número inteiro: ")
r = leiaFloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {n} e o real foi {r} ")


