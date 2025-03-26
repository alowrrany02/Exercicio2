class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_salario(self) -> float:
        return self.salario_base


class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        return self.salario_base * 1.25  # Bônus de 25%


class Desenvolvedor(Funcionario):
    def calcular_salario(self) -> float:
        return self.salario_base * 1.15  # Bônus de 15%


# Exemplo de uso:
funcionario = Funcionario("João Silva", 5000)
print(f"{funcionario.nome} - Salário: R${funcionario.calcular_salario():.2f}")
# Saída: João Silva - Salário: R$5000.00

gerente = Gerente("Maria Santos", 8000)
print(f"{gerente.nome} - Salário: R${gerente.calcular_salario():.2f}")
# Saída: Maria Santos - Salário: R$10000.00

dev = Desenvolvedor("Carlos Oliveira", 6000)
print(f"{dev.nome} - Salário: R${dev.calcular_salario():.2f}")
# Saída: Carlos Oliveira - Salário: R$6900.00