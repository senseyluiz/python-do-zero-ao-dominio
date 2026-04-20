# 35
# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
retaA = float(input("Digite o comprimento da reta A: "))
retaB = float(input("Digite o comprimento da reta B: "))
retaC = float(input("Digite o comprimento da reta C: "))
tri = False
if retaA + retaB > retaC and retaA + retaC > retaB and retaC + retaB > retaA :
    tri = True

print (f"Com os comprimento de reta:\n"
          f"RetaA = {retaA}\n"
          f"RetaB = {retaB}\n"
          f"RetaC = {retaC}\n")
if tri:
    print(
          f"Essas retas formam um TRIÂNGULO")
else:
    print(
          f"Essas retas NÃO formam um TRIÂNGULO")