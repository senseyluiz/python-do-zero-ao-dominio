# 104
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função imput() do python
# porém fazendo a validação para aceitar apenas um valor numérico

def leiaInt(msg=""):
    while True:
        n = input(msg)
        if not n.isnumeric():
            print("\33[31mERRO! Digite um número inteiro válido\33[m")
        else:
            break
    return int(n)


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n} ")

