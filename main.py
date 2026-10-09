from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá mundo"}

@app.get("/saudacao/{nome}")
def saudacao(nome:str):
    return {"mensagem": f"Olá, {nome}"}

@app.get("/soma")
def soma(a:int, b:int):
    return {"A soma é": a+b}

#http://localhost:8000/soma?a=abc&b=10
#{
#  "detail": [
#    {
#      "type": "int_parsing",
#      "loc": [
#        "query",
#        "a"
#      ],
#      "msg": "Input should be a valid integer, unable to parse string as an integer",
#      "input": "abc"
#    }
#  ]
#}

class Usuario(BaseModel):
    nome: str
    email: str
    idade: int

@app.post("/usuarios")
def usuarios(usuario:Usuario):
    return usuario  
