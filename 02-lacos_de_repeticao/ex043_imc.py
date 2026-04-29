# 043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu Índice de Massa Corporal(IMC) e mostre seus status,
# Conforme a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
from time import sleep
print("==== CALCULADORA DE MASSA CORPORAL ====")

nome = input("Digite seu nome: ").strip()
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
IMC = peso / (altura * altura)
if IMC < 18.5:
    categoria = "ABAIXO DO PESO"
elif IMC < 25:
    categoria = "PESO IDEAL"
elif IMC < 30:
    categoria = "SOBREPESO"
elif IMC < 40:
    categoria = "OBESIDADE"
else:
    categoria = "OBESIDADE MÒRBITA"
print("CALCULANDO SUA MASSA CORPORAL ...")
sleep(2)
print(f"{nome} seu IMC é de {IMC:.1f}: {categoria}")
