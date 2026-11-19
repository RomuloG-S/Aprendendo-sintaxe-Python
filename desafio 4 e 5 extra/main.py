from typing import Annotated
from fastapi import FastAPI, APIRouter, HTTPException, status, Path
from model import ProdutoCreate, ProdutoResponse

#definindo as rotas, calculadora e rota produto
calculadora = APIRouter(prefix = "/calculadora", tags = ["calculadora"])
produto = APIRouter(prefix="/produto", tags = ["produto"])
#criando o app, é a base e só se cria uma vez
app = FastAPI()

@app.get("/status")
def status():
    return {"status": "Online", "Versão": 1.0}

@calculadora.get("/somar")
def soma(a:int, b:int):
    return {"soma" : a + b}
@calculadora.get("/subtrair")
def subtração(a:int, b:int):
    return {"subtração" : a - b}
@calculadora.get("/multiplicar")
def multiplicação(a:int, b:int):
    return {"produto" : a * b}
@calculadora.get("/dividir")
def divisão(a:int, b:int):
    if b <= 0:
        raise HTTPException(
        status_code=status.HTTP404_NOT_FOUND,
        detail= "dado inválido"
        )
    return {"divisão" : a/b}

@app.get("/produtos/{produto_id}")
def get_produto(produto:int):
    if produto <= 0:
        raise HTTPException(
            status_code=status.HTTP404_BAD_REQUEST,
            detail = "dado invalido"
        )
    return {"produto" : "encontrado"}

@app.get("/busca")
def busca(nome = None):
    if nome == None:
        return {"mensagem": "nenhum filtro aplicao"}
    if nome != None:
        return {"mensagem": f"Buscando por {nome}"}

@app.get("/usuarios/{usuario_id}/post")
def forms(usuario, limite: Annotated[int, Path(ge = 0, le = 100)] = 10, ordem:str = "recentes"):
    return {"formulario" f"{usuario, limite, ordem}"}
p1 = {
    "id": 1,
    "nome": "faca",
    "preco": 10,
    "categoria": "cozinha"
}
p2 = {
    "id": 2,
    "nome": "garfo",
    "preco": 10,
    "categoria": "cozinha"
}
p3 = {
    "id": 3,
    "nome": "colher",
    "preco": 10,
    "categoria": "cozinha"
}
p4 = {
    "id": 4,
    "nome": "celular",
    "preco": 1000,
    "categoria": "eletronico"
}
p5 = {
    "id": 5,
    "nome": "playstation",
    "preco": 4000,
    "categoria": "eletronico"
}

lista = [p1, p2, p3, p4, p5]

#endpoint para listar todos produtos da lista que foi definida acima
@produto.get("/todos")
def todos(categoria:str = None, preco:int = None):
    #filtro 1: listar todos já que não tem filtro
    if categoria == None and preco == None:
        return lista
    #filtro 2: listar filtro duplo, obrigado a usar os 2 filtros
    if categoria != None and preco != None:
            produto_filtrado = []
            for produto in lista:
                if categoria == produto["categoria"]:
                    if produto["preco"] < preco:
                        produto_filtrado.append(produto)
            return produto_filtrado
    #filtro 3: filtrar só por categoria
    if categoria != None:
        produto_cat = []
        for produto in lista:
            if categoria == produto["categoria"]:
                produto_cat.append(produto)
        return produto_cat
    #filtro 4: filtrar só por preço
    if preco != None:
        produto_pre = []
        for produto in lista:
            if produto["preco"] < preco:
                produto_pre.append(produto)
        return produto_pre

@produto.get("/{produto_id}")
#filtrar por id
def item_especifico(id:int):
    for produto in lista:
        if id == produto["id"]:
            return produto
    else:
        #informando o erro que deu caso não encontre o id
        raise HTTPException(
            #status 404 Not Found
                        status_code=404, detail="Produto não encontrado"
                    )

@app.post("/produtos")
#tem que inserir o parametro e usar o model como modelo mesmo, igual usar int ou str
#e como é um post, os dados vão ser inseridos no swagger
def produto_model(produto: ProdutoCreate, status_code=201, response_model=ProdutoResponse):
    return {"Mensagem": "Produto criado", "Produto": produto}


#usado para definir e diminuir a rota
app.include_router(calculadora)
app.include_router(produto)