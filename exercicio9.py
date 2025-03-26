class Item:
    def __init__(self, descricao: str, preco: float):
        self.descricao = descricao
        self.preco = preco
    
    def exibir(self):
        return f"{self.descricao}: R${self.preco:.2f}"


class Pedido:
    def __init__(self, numero: int):
        self.numero = numero
        self.itens = [] 
    
    def adicionar_item(self, item: Item):
        """Adiciona um item ao pedido (composição)"""
        self.itens.append(item)
        print(f"Item '{item.descricao}' adicionado ao pedido {self.numero}")
    
    def calcular_total(self) -> float:
        """Calcula o valor total do pedido"""
        return sum(item.preco for item in self.itens)
    
    def exibir_pedido(self):
        """Exibe todos os itens e o total do pedido"""
        print(f"\nPedido #{self.numero}")
        print("Itens:")
        for item in self.itens:
            print(f"- {item.exibir()}")
        print(f"Total: R${self.calcular_total():.2f}")


item1 = Item("Camiseta", 49.90)
item2 = Item("Calça Jeans", 129.90)
item3 = Item("Tênis", 199.90)

pedido123 = Pedido(123)

pedido123.adicionar_item(item1)
pedido123.adicionar_item(item2)
pedido123.adicionar_item(item3)


pedido123.exibir_pedido()


print("\nSe o pedido for removido, seus itens deixam de existir no contexto desse pedido")
print("(Os objetos Item continuam existindo apenas se referenciados em outros lugares)")