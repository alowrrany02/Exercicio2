class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
    
    def exibir_info(self) -> str:
        return f"{self.nome}: R${self.salario:.2f}"


class Departamento:
    def __init__(self, nome: str):
        self.nome = nome
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
    
    def calcular_salario_total(self) -> float:
        return sum(funcionario.salario for funcionario in self.funcionarios)


def test_departamento_integracao():

    depto_rh = Departamento("Recursos Humanos")
    

    funcionario1 = Funcionario("João Silva", 5000.00)
    funcionario2 = Funcionario("Maria Santos", 6500.50)
    funcionario3 = Funcionario("Carlos Oliveira", 4200.75)
    
    depto_rh.adicionar_funcionario(funcionario1)
    depto_rh.adicionar_funcionario(funcionario2)
    depto_rh.adicionar_funcionario(funcionario3)
    

    salario_total = depto_rh.calcular_salario_total()
    total_esperado = 5000.00 + 6500.50 + 4200.75
    
    print("\n=== Teste de Integração ===")
    print(f"Salário total calculado: R${salario_total:.2f}")
    print(f"Salário total esperado: R${total_esperado:.2f}")
    
  
    assert abs(salario_total - total_esperado) < 0.01, "Erro no cálculo do salário total"
    
   
    print("\nFuncionários no departamento:")
    for func in depto_rh.funcionarios:
        info = func.exibir_info()
        print(info)
        assert func.nome in info and str(func.salario) in info, "Erro no método exibir_info()"
    
    print("\n✅ Teste de integração passou com sucesso!")


if __name__ == "__main__":
    test_departamento_integracao()