class ContaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.__saldo = 0.0  
    
    def depositar(self, valor: float):
        """Adiciona o valor ao saldo da conta"""
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor: float):
        """Remove o valor do saldo, se houver saldo suficiente"""
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def get_saldo(self) -> float:
        """Método getter para obter o saldo atual"""
        return self.__saldo
    
    def __str__(self):
        return f"Titular: {self.titular}, Saldo: R${self.__saldo:.2f}"

conta = ContaBancaria("Maria Oliveira")

print(conta) 

conta.depositar(1000)

print(f"Saldo atual: R${conta.get_saldo():.2f}")

conta.sacar(300)

print(f"Saldo após saque: R${conta.get_saldo():.2f}")