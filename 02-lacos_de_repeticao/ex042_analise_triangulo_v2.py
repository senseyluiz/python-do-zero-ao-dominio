# 042
# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais e um diferente
# Escaleno: todos os lados diferentes

retaA = float(input("Digite o comprimento da reta A: "))
retaB = float(input("Digite o comprimento da reta B: "))
retaC = float(input("Digite o comprimento da reta C: "))
tri = False
if retaA + retaB > retaC and retaA + retaC > retaB and retaC + retaB > retaA :
    tri = True
    if retaA == retaB == retaC:
        tipo = "EQUILÁTERO"
    elif retaA == retaB != retaC or retaB == retaC != retaA or retaA == retaC !=retaB:
        tipo = "ISÓSCELES"
    else:
        tipo = "ESCALENO"

print (f"Com os comprimento de reta:\n"
          f"RetaA = {retaA}\n"
          f"RetaB = {retaB}\n"
          f"RetaC = {retaC}\n")
if tri:
    print(
          f"Essas retas formam um TRIÂNGULO {tipo}")
else:
    print(
          f"Essas retas NÃO formam um TRIÂNGULO")