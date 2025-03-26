class ContaBancaria:
    def __init__(self):
        self.__saldo = 0.0
    
    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.__saldo += valor
    
    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar o saque")
        self.__saldo -= valor
    
    def get_saldo(self) -> float:
        return self.__saldo


import unittest

class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        """Executado antes de cada teste"""
        self.conta = ContaBancaria()
    
    def test_deposito_aumenta_saldo(self):
        self.conta.depositar(100.0)
        self.assertEqual(self.conta.get_saldo(), 100.0)
    
    def test_saque_reduz_saldo(self):
        self.conta.depositar(200.0)
        self.conta.sacar(50.0)
        self.assertEqual(self.conta.get_saldo(), 150.0)
    
    def test_saque_saldo_insuficiente(self):
        self.conta.depositar(30.0)
        with self.assertRaises(ValueError):
            self.conta.sacar(50.0)
        self.assertEqual(self.conta.get_saldo(), 30.0)  # Saldo não deve mudar
    
    def test_deposito_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.conta.depositar(-10.0)
    
    def test_saque_valor_negativo(self):
        self.conta.depositar(100.0)
        with self.assertRaises(ValueError):
            self.conta.sacar(-20.0)


if __name__ == '__main__':
    unittest.main()