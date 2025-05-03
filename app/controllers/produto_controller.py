from fastapi import APIRouter, HTTPException
from repositories import produto_repository
from schemas import ProdutoCreate, ProdutoUpdate, ProdutoOut
from typing import List

router = APIRouter()

@router.get("/produtos", response_model=List[ProdutoOut])
def listar_produtos():
    try:
        produtos = produto_repository.listar_produtos()
        return [
            ProdutoOut(id=p[0], nome=p[1], quantidade=p[2], imagem=None) for p in produtos
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/produtos", response_model=ProdutoOut)
def adicionar_produto(produto: ProdutoCreate):
    try:
        produto_repository.adicionar_produto(produto.nome, produto.quantidade)
        # Simulando retorno, já que a função original não retorna o novo produto:
        return ProdutoOut(id=0, nome=produto.nome, quantidade=produto.quantidade, imagem=None)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar produto: {str(e)}")

@router.put("/produtos/{id}", response_model=ProdutoOut)
def editar_produto(id: int, produto: ProdutoUpdate):
    try:
        produto_repository.editar_produto(id, produto.nome, produto.quantidade)
        return ProdutoOut(id=id, nome=produto.nome, quantidade=produto.quantidade, imagem=None)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao editar produto: {str(e)}")

@router.delete("/produtos/{id}")
def deletar_produto(id: int):
    try:
        produto_repository.deletar_produto(id)
        return {"mensagem": "produto deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"erro ao deletar produto: {str(e)}")
