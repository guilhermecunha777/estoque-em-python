from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import io
import csv

from repositories import produto_repository
from controllers import produto_controller

app = FastAPI(title="Sistema de Controle de Estoque")

# Inclui as rotas do controller
app.include_router(produto_controller.router)

@app.get("/relatorio/csv", summary="Gerar relatório CSV de produtos")
def gerar_relatorio_csv_api():
    try:
        produtos = produto_repository.listar_produtos()

        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow(["ID", "Nome", "Quantidade"])
        for prod in produtos:
            writer.writerow(prod[:3])

        buffer.seek(0)
        return StreamingResponse(
            buffer,
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=relatorio_estoque.csv"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar relatório: {str(e)}")
