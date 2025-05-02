from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from repositories import produto_repository
from controllers import produto_controller
from fastapi.responses import StreamingResponse
import io
import csv

app = FastAPI()

app.include_router(produto_controller.router)

class produto(BaseModel):
    nome: str
    quantidade: int

@app.get("/produtos", operation_id="listar_produtos")
def listar_produtos():
    return produto_repository.buscar_todos_produtos()

@app.post("/produtos", operation_id="adicionar_produto")
def adicionar_produto(produto: produto):
    produto_repository.adicionar_produto(produto.nome, produto.quantidade)
    return {"mensagem": "produto adicionado com sucesso."}

@app.put("/produtos/{id}", operation_id="editar_produto")
def editar_produto(id: int, produto: produto):
    produto_repository.editar_produto(id, produto.nome, produto.quantidade)
    return {"mensagem": "produto atualizado com sucesso."}

@app.delete("/produtos/{id}", operation_id="deletar_produto")
def deletar_produto(id: int):
    produto_repository.deletar_produto(id)
    return {"mensagem": "produto deletado com sucesso."}

@app.get("/relatorio/csv", summary="Gerar relatório CSV de produtos")
def gerar_relatorio_csv_api():
    try:
        produto = produto_repository.listar_produtos()
        
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow(["ID","Nome","Quantidade"])
        for prod in produto:
            writer.writerow(prod[:3])
        
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="text/csv",  headers={"Content-Disposition": "attachment; filename=relatorio_estoque.csv"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar relatório: {str(e)}")