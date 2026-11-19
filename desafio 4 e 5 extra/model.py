from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome:str = Field(min_length=3, max_length=50)
    preco:int = Field(gt=0)
    categoria:str
    em_estoque:bool = True

class ProdutoResponse(ProdutoCreate):
    id:int