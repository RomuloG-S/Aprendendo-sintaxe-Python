from typing import Annotated
from fastapi import FastAPI, APIRouter, HTTPException, Query
import json
app = FastAPI()
produto = APIRouter(prefix="/prod", tags=["Produtos"])
calculadora = APIRouter(prefix="/calc", tags=["Calculadora"])
@app.get("/")
def status():
    return {"status": "online", "versão": 1.0}

@calculadora.get("/soma")
def soma(a:int, b:int):
    return {"soma": a+b}

@calculadora.get("/subtracao")
def subtracao(a:int, b:int):
    return {"Subtração": a-b}

@calculadora.get("/multiplicacao")
def multiplicacao(a:int, b:int):
    return {"Multiplicação": a*b}

@calculadora.get("/divisao")
def divisao(a:int, b:int):
    if b <= 0:
        return HTTPException(status_code=404, detail="insira um divisor maior que 0")
    return {"Divisão": a/b}

@produto.get("/produtos/{produto_id}")
def Procurar_Produto(p_id:int):
    if p_id <= 0:
        return HTTPException(status_code=404, detail="insira um id maior que 0")
    return {"mensagem": "Produto encontrado"}

#Please correct the following validation errors and try again.
#For 'p_id': Value must be an integer.

@produto.get("/busca")
def Busca(nome:str | None = None):
    if nome is None:
        return {"mensagem": "Nenhum filtro aplicado"}
    return {"mensagem": f"Buscando por {nome}"}

@produto.get("/usuarios/{usuario_id}/posts")
def seila(u_id:int, limite:Annotated[int | None , Query(ge=0, le=100)] = None, ordem:str = None):
    forms = {"u_id":u_id,
             "limite":limite,
             "ordem":ordem}
    return {"mensagem": forms}

produtos = []

item1 = {
    "id":1,
    "nome":"bola",
    "preço":100,
    "categoria":"esporte"
},
item2 = {
    "id":2,
    "nome":"boneca",
    "preço":150,
    "categoria":"brinquedo"
}
item3 = {
    "id":3,
    "nome":"prato",
    "preço":30,
    "categoria":"cozinha"
}
item4 = {
    "id":4,
    "nome":"garfo",
    "preço":5,
    "categoria":"cozinha"
}
item5 = {
    "id":5,
    "nome":"faca",
    "preço":5,
    "categoria":"cozinha"
}
item5 = {
    "id":5,
    "nome":"faca",
    "preço":5,
    "categoria":"cozinha"
}          
item6 = {
    "id":6,
    "nome":"mouse",
    "preço":99,
    "categoria":"eletronica"
}              
produtos.extend([item1, item2, item3, item4, item5, item6])
@produto.get("/produtos")
def Listar_Produtos(categoria: str, preço: int):
    resultado = []
    
    for produto in produtos:
        if isinstance(produto, str):
            try:
                produto = json.loads(produto)
            except:
                continue
                
        if isinstance(produto, dict):
            prod_categoria = produto.get("categoria")
            prod_nome = produto.get("nome")
            prod_preço = produto.get("preço")
            
            if categoria == prod_categoria and prod_preço is not None and preço > prod_preço:
                
                resultado.append({
                    "categoria": prod_categoria,
                    "nome": prod_nome,
                    "preço": prod_preço
                })
    return {"categoria buscada": categoria, "preço maximo": preço, "itens encontrados": resultado}


app.include_router(calculadora)
app.include_router(produto)