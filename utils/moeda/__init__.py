def metade(valor):
    return valor / 2

def dobro(valor):
    return valor * 2

def aumentar(valor, porcentagem):
    return valor + (valor * porcentagem / 100)

def diminuir(valor, porcentagem):
    return valor - (valor * porcentagem / 100)

def moeda(valor, formato=True):
    if formato:
        return f"R${valor:.2f}".replace('.', ',')
    else:
        return valor
def resumo(valor=0, aumento=10, reducao=5):
    print("-" * 40)
    print(f"{'RESUMO DO VALOR'.center(40)}")
    print("-" * 40)
    print(f"{'PREÇO ANALISADO:':<25}{moeda(valor):<12}\n"
          f"{'DOBRO DO PREÇO:':<25}{moeda(dobro(valor)):<12}\n"
          f"{'METADE DO PREÇO:':<25}{moeda(metade(valor)):<12}\n"
          f"{f'{aumento}% DE AUMENTO:':<25}{moeda(aumentar(valor, aumento)):<12}\n"
          f"{f'{reducao}% DE REDUÇÃO:':<25}{moeda(diminuir(valor, reducao)):<12}")
    print("-" * 40)