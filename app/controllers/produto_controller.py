from fastapi import APIRouter, HTTPException
from typing import List
from schemas import ProdutoCreate, ProdutoUpdate, ProdutoOut
from repositories import produto_repository

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.get("/", response_model=List[ProdutoOut], summary="Listar todos os produtos")
def listar_produtos():
    try:
        produtos = produto_repository.listar_produtos()
        return produtos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar produtos: {str(e)}")

@router.post("/", response_model=ProdutoOut, summary="Adicionar um novo produto")
def adicionar_produto(produto: ProdutoCreate):
    try:
        novo_produto = produto_repository.adicionar_produto(produto.nome, produto.quantidade)
        return novo_produto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar produto: {str(e)}")

@router.put("/{id}", response_model=ProdutoOut, summary="Editar um produto existente")
def editar_produto(id: int, produto: ProdutoUpdate):
    try:
        produto_atualizado = produto_repository.editar_produto(id, produto.nome, produto.quantidade)
        return produto_atualizado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao editar produto: {str(e)}")

@router.delete("/{id}", summary="Deletar um produto")
def deletar_produto(id: int):
    try:
        produto_repository.deletar_produto(id)
        return {"mensagem": "Produto deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar produto: {str(e)}")
