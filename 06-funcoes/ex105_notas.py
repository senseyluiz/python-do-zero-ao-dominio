# 105
# Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também Docstring à função

def notas(*notas, sit=False):
    """
    — > Função para analisar notas e situação de vários alunos,
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    global situacao
    total = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / total
    if media < 5:
        situacao = "RUIM"
    if media >= 5:
        situacao = "RAZOÁVEL"
    if media >= 7:
        situacao = "BOA"
    if sit:
        boletim = {
            "total" : total,
            "maior" : maior,
            "menor" : menor,
            "media" : media,
            "situacao" : situacao
        }
    else:
        boletim = {
            "total" : total,
            "maior" : maior,
            "menor" : menor,
            "media" : media,
        }
    return boletim



resp = notas(0, 2, 6.5, 7, 8)
print(resp)