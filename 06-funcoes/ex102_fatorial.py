# 102
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# O primeiro que indique o número a calcular e o
# outro chamado "show", que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(n, show=False):
    """
    — > Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor fatorial de um número n
    """
    fatorial = 1

    for c in range(n, 0, -1):
        fatorial *= c
        if show:
            if c == 1:
                print(f"{c} = ", end="")
            else:
                print(f"{c} x ", end="")
    return fatorial


print(fatorial(10, True))
print(fatorial(5))
help(fatorial)
