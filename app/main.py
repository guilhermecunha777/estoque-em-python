from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
import io
import csv

from app.repositories import produto_repository
from app.controllers import produto_controller
from database.init_db import inicializar_banco

app = FastAPI(title="Sistema de Estoque")

inicializar_banco()

app.include_router(produto_controller.router)

class ProdutoIn(BaseModel):
    nome: str
    quantidade: int

# Rota adicional para gerar relatório em CSV
@app.get("/relatorio/csv", summary="Gerar relatório CSV de produtos")
def gerar_relatorio_csv():
    try:
        produtos = produto_repository.listar_produtos()

        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow(["ID", "Nome", "Quantidade"])
        for prod in produtos:
            writer.writerow(prod[:3])

        buffer.seek(0)
        return StreamingResponse(buffer, media_type="text/csv",
                                headers={"Content-Disposition": "attachment; filename=relatorio_estoque.csv"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar relatório: {str(e)}")
