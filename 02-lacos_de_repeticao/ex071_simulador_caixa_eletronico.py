# 071
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte qual será o valor a ser sacado(número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cedulas de R$50,00, R$20,00, R$10,00 e R$1,00

print("=" *40)
print(f"{"BANCO JUSTO":^40}")
print("=" *40)

valor = int(input("Qual o valor você quer sacar: "))
total = valor
ced = 50
cont= 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f"Total de {cont} cédulas de R$ {ced:.2f}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break
print("Volte sempre ao BANCO JUSTO! Tenha um bom dia!")