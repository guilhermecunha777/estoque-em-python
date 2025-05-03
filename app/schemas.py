from pydantic import BaseModel
from typing import Optional

class ProdutoBase(BaseModel):
    nome: str
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(ProdutoBase):
    id: int

class ProdutoOut(ProdutoBase):
    id: int
    imagem: Optional[str] = None

    class Config:
        from_attributes = True
