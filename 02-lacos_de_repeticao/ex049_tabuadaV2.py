# 049
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, contudo, agora utilizando um laço FOR

n = int(input("Digite um número para ver sua tabuada: "))
print(f"=== TABUADA DO NÚMERO: {n} ===")
for i in range (1, 11):
    print(f"{n} x {i:2} = {n*i:2}")