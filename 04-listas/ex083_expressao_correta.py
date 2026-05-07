expressao = input("Digite sua expressão: ")
pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop() # Remove o último '(' aberto
        else:
            pilha.append(')') # Adiciona um erro para indicar que fechou sem abrir
            break

if len(pilha) == 0:
    print("Sua expressão está correta!")
else:
    print("Sua expressão está errada.")