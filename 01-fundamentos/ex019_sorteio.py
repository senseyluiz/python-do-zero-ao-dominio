# 019
# Um professor que sortear um dos seus 4 alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
al1 = input("Digite o primeiro aluno: ")
al2 = input("Digite o segundo aluno: ")
al3 = input("Digite o terceiro aluno: ")
al4 = input("Digite o quarto aluno: ")
sorteado = random.choice((al1, al2, al3, al4))
print(f"O aluno sorteado foi {sorteado}")