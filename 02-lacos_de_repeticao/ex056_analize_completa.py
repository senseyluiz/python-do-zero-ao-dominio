# 056
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos

dados = []
soma_idade = 0
mulheres = 0
homem_mais_velho = "Você não informou nenhum homem"
idade_maior = 0
for i in range(1, 5):
    print(f"----- {i}º Pessoa -----")
    nome = str(input(f"Nome: "))
    idade = int(input(f"Idade: "))
    sexo = str(input(f"Sexo: ")).upper()
    dado = (nome, idade, sexo)
    dados.append(dado)

print("==" * 10)
for i in dados:
    soma_idade += i[1]
    if i[2] == "F":
        if i[1] < 20:
            mulheres += 1
    if i[2] == "M":
        if idade_maior < i[1]:
            idade_maior = i[1]
            homem_mais_velho = i[0]

media = soma_idade / len(dados)
print(f"Média de idades: {media} anos\n"
      f"Quantidade de mulheres com menos de 20 anos: {mulheres}\n"
      f"Homem mais velho: {homem_mais_velho} de {idade_maior} anos")