class Medico:
    def __init__(self, nome: str, especialidade: str):
        self.nome = nome
        self.especialidade = especialidade
    
    def __str__(self):
        return f"Dr. {self.nome} ({self.especialidade})"


class Paciente:
    def __init__(self, nome: str, idade: int, medico: Medico):
        self.nome = nome
        self.idade = idade
        self.medico = medico  
    
    def exibir_informacoes(self):
        print(f"Paciente: {self.nome}, {self.idade} anos")
        print(f"Médico responsável: {self.medico}")  


cardiologista = Medico("Carlos Silva", "Cardiologia")
pediatra = Medico("Ana Oliveira", "Pediatria")


paciente1 = Paciente("João Santos", 45, cardiologista)
paciente2 = Paciente("Maria Souza", 8, pediatra)


print("=== Informações dos Pacientes ===")
paciente1.exibir_informacoes()
print()
paciente2.exibir_informacoes()


print("\n=== Demonstração de independência ===")
outro_medico = Medico("Paula Rocha", "Clínico Geral")
paciente1.medico = outro_medico  
paciente1.exibir_informacoes()