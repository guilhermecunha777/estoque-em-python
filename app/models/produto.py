class Produto:
    def __init__(self, id: int, nome: str, quantidade: int, imagem: str = Nones):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.imagem = imagem

    def __str__(self):
        return f"<produto id={self.id}, nome={self.nome}, quantidade={self.quantidade}, imagem={self.imagem}>"
