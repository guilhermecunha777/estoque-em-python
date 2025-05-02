from fastapi import APIRouter, HTTPException
from repositories import produto_repository
from schemas import ProdutoCreate, ProdutoUpdate, ProdutoOut
from typing import List

router = APIRouter()

@router.get("/produtos", response_model=List[ProdutoOut])
def listar_produtos():
    produtos = produto_repository.listar_produtos()
    return produtos

@router.post("/produtos", response_model=ProdutoOut)
def adicionar_produto(produto: ProdutoCreate):
    try:
        novo_produto = produto_repository.adicionar_produto(produto.nome, produto.quantidade)
        return novo_produto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar produto: {str(e)}")

@router.put("/produtos/{id}", response_model=ProdutoOut)
def editar_produto(id: int, produto: ProdutoOut):
    try:
        produto_atualizado = produto_repository.adicionar_produto(id, produto.nome, produto.quantidade)
        return produto_atualizado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao editar produto: {str(e)}")

@router.delete("/produtos/{id}")
def deletar_produto(id: int):
    try:
        produto_repository.deletar_produto(id)
        return {"mensagem": "produto deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"erro ao deletar produto: {str(e)}")