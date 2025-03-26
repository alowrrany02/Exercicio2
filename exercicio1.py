class Livro:
    def __init__(self, titulo:str, autor:str, ano_publicacao:int):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def exibir_infor(self) -> str:
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}"
    
meu_livro = Livro(
    titulo = "Vidas Secas",
    autor = "Graciliano Ramos",
    ano_publicacao = 1938
)

print(meu_livro.exibir_infor())