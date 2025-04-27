class Produto:
    def __init__(self, id, nome, quantidade, caminho_foto):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.caminho_foto = caminho_foto

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Quantidade: {self.quantidade} | Foto: {self.caminho_foto}"
