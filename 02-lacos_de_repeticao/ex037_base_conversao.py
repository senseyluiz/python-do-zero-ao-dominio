# 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para BINARIO
# - 2 para OCTAL
# - 3 para hexadecimal
num = int(input("Digite um número inteiro: "))
print(f"Escolha uma opção para converter o número {num}:\n"
      "1 - BINÁRIO\n"
      "2 - OCTAL\n"
      "3 - HEXADECIMAL")

opcao = int(input("Opção: "))
if opcao == 1:
    conversão = bin(num)
    escolha = "BINÁRIO"
elif opcao == 2:
    conversão = oct(num)
    escolha = "OCTAL"
elif opcao == 3:
    conversão = hex(num)
    escolha = "HEXADECIMAL"
else:
    print("Opção incorreta.")

print(f"O numero {num} convertido para {escolha} é: {conversão}")