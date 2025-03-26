class Tarefa:
    def __init__(self, descricao: str):
        self.descricao = descricao
        self.status = "Pendente"  
    
    def atualizar_status(self, novo_status: str):
        self.status = novo_status
    
    def __str__(self):
        return f"{self.descricao} - {self.status}"


class Projeto:
    def __init__(self, nome: str):
        self.nome = nome
        self.tarefas = []  
    
    def adicionar_tarefa(self, tarefa: Tarefa):
        """Adiciona uma tarefa existente ao projeto"""
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa.descricao}' adicionada ao projeto '{self.nome}'")
    
    def exibir_tarefas(self):
        """Exibe todas as tarefas do projeto"""
        print(f"\nTarefas do projeto '{self.nome}':")
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada")
        else:
            for i, tarefa in enumerate(self.tarefas, 1):
                print(f"{i}. {tarefa}")


tarefa1 = Tarefa("Desenvolver interface")
tarefa2 = Tarefa("Testar funcionalidades")
tarefa3 = Tarefa("Documentar código")

projeto_web = Projeto("Site Corporativo")


projeto_web.adicionar_tarefa(tarefa1)
projeto_web.adicionar_tarefa(tarefa2)


projeto_web.exibir_tarefas()

tarefa1.atualizar_status("Em andamento")

projeto_web.exibir_tarefas()

print("\nTarefa independente:")
print(tarefa3) 