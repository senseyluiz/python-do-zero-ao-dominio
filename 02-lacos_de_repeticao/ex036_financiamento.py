# 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de um casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Salário do comprador: R$"))
anos = int(input("Em quantos anos que pagar: "))
qtd_prestacao= 12 * anos
valor_prestacao = valor_casa / qtd_prestacao
aprovado = "Negado"

if valor_prestacao < salario_comprador * 0.30:
    aprovado = "Aprovado"

print(f"=== FINANCIAMENTO IMOBILIARIO ===")
print(f"Valor da Casa: R${valor_casa:.2f}\n"
      f"Salario do comprador: {salario_comprador:.2f}\n"
      f"Quantidade de prestação: {qtd_prestacao}\n"
      f"Valor da Prestação: R${valor_prestacao:.2f}\n"
      f"Emprestimo: {aprovado}")
