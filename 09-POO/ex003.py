class ContaBancaria:
    """
    Essa classe cria uma conta bancária com id, nome e saldo e permite fazer saque e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"Nome: {self.nome}, Saldo: R${self.saldo:,.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} reais realizado com \33[32mSUCESSO\33[0m")

    def sacar(self, valor):
        if self.saldo <= valor:
            print ("Saldo insuficiente!!!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} reais realizado com \33[32mSUCESSO\33[0m")
luis = ContaBancaria(110, "Luis", 5000)
lucas = ContaBancaria(111, "Lucas", 3000)

print(luis)
print(lucas)
luis.depositar(1500)
