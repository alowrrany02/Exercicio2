from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float) -> float:
        pass


class CartaoCredito(Pagamento):
    def processar_pagamento(self, valor: float) -> float:
        taxa = 5.00  
        total = valor + taxa
        print(f"Pagamento com Cartão de Crédito: R${valor:.2f} + taxa de R${taxa:.2f} = R${total:.2f}")
        return total


class CartaoDebito(Pagamento):
    def processar_pagamento(self, valor: float) -> float:
        print(f"Pagamento com Cartão de Débito: R${valor:.2f} (sem taxas)")
        return valor


class Dinheiro(Pagamento):
    def processar_pagamento(self, valor: float) -> float:
        if valor > 100.00:
            desconto = valor * 0.10 
            total = valor - desconto
            print(f"Pagamento em Dinheiro: R${valor:.2f} - desconto de R${desconto:.2f} = R${total:.2f}")
            return total
        else:
            print(f"Pagamento em Dinheiro: R${valor:.2f} (sem desconto para valores ≤ R$100,00)")
            return valor


print("\n=== Processamento de Pagamentos ===")


credito = CartaoCredito()
valor_final = credito.processar_pagamento(150.00)
print(f"Valor a cobrar: R${valor_final:.2f}\n")


debito = CartaoDebito()
valor_final = debito.processar_pagamento(150.00)
print(f"Valor a cobrar: R${valor_final:.2f}\n")


dinheiro1 = Dinheiro()
valor_final = dinheiro1.processar_pagamento(120.00)
print(f"Valor a cobrar: R${valor_final:.2f}\n")


dinheiro2 = Dinheiro()
valor_final = dinheiro2.processar_pagamento(80.00)
print(f"Valor a cobrar: R${valor_final:.2f}\n")