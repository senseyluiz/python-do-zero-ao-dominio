# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

digitado = input("Digite algo: ")
print(f"{digitado} é do tipo: {type(digitado)}\n"
      f"{digitado} é um número: {digitado.isnumeric()}\n"
      f"{digitado} é um alfabeto: {digitado.isalpha()}\n"
      f"{digitado} é alfanumérico: {digitado.isalnum()}\n"
      f"{digitado} é está minúsculo: {digitado.islower()}\n"
      f"{digitado} é está maiúsculo: {digitado.isupper()}\n"
      f"{digitado} é está capitalizado: {digitado.istitle()}\n"
      f"{digitado} contém espaço: {digitado.isspace()}\n")