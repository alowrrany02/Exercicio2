class ContaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.0
    
    def depositar(self, valor: float):
        """Adiciona o valor ao saldo da conta"""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor: float):
        """Remove o valor do saldo, se houver saldo suficiente"""
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def __str__(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}"

conta = ContaBancaria("João Silva")

print(conta) 

conta.depositar(500.50)

conta.depositar(-100)  

conta.sacar(200.75)

conta.sacar(400)

print(conta)  