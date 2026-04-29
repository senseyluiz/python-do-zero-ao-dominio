# 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
print("==== Lojas ROCHA, aqui você tem qualidade ====")
preco = float(input("Preço das compras: R$"))
total = preco
print("FORMA DE PAGAMENTO\n"
      "[1] à vista dinheiro/cheque\n"
      "[2] à vista cartão\n"
      "[3] 2x no cartão\n"
      "[4] 3x ou mais no cartão")
opcao = input("Qual sua opção? ")
if opcao == "1":
    total = preco * 0.90
elif opcao == "2":
    total = preco * 0.95
elif opcao == "3":
    total = preco
    parcela = total / 2
    print(f"Sua compra será parcelada de 2x de R${parcela:.2f}")
elif opcao == "4":
    total = preco * 1.20
    parcela = total / 3
    print(f"Sua compra será parcelada de 3x de R${parcela:.2f}")
else:
    print("OPÇÃO INCORRETA. Tente novamente.")

print(f"Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.")