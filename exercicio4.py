class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
    
    def exibir_info(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, num_portas: int):
        super().__init__(marca, modelo)  
        self.num_portas = num_portas
    
    def exibir_info(self) -> str:
        info_veiculo = super().exibir_info()
        return f"{info_veiculo}, Número de portas: {self.num_portas}"


meu_veiculo = Veiculo("Ford", "F-100")
print(meu_veiculo.exibir_info())

meu_carro = Carro("Toyota", "Corolla", 4)
print(meu_carro.exibir_info())