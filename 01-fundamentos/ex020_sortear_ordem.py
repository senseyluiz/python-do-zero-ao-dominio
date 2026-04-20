# 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
al1 = input("Digite o primeiro aluno: ")
al2 = input("Digite o segundo aluno: ")
al3 = input("Digite o terceiro aluno: ")
al4 = input("Digite o quarto aluno: ")
lista = [al1, al2, al3, al4]
sorteado = random.sample(lista, len(lista))
print(f"A ordem sorteada é: {sorteado}")