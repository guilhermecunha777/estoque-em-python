from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from repositories import produto_repository

app = FastAPI()

class produto(BaseModel):
    nome: str
    quantidade: int

@app.get("/produtos")
def listar_produtos():
    return produto_repository.buscar_todos_produtos()

@app.post("/produtos")
def adicionar_produto(produto: produto):
    produto_repository.adicionar_produto(produto.nome, produto.quantidade)
    return {"mensagem": "produto adicionado com sucesso."}

@app.put("/produtos/{id}")
def editar_produto(id: int, produto: produto):
    produto_repository.editar_produto(id, produto.nome, produto.quantidade)
    return {"mensagem": "produto atualizado com sucesso."}

@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    produto_repository.deletar_produto(id)
    return {"mensagem": "produto deletado com sucesso."}
