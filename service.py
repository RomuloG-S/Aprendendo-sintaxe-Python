import json
def calcular_media(notas:list) -> float:
    soma = 0.0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media


def adicionar_usuario(lista:list, id:int, nome:str, email:str) -> list:
    formulario = {
        "id":id,
        "nome":nome,
        "email":email
    }
    lista.append(formulario)
    return lista

#print(lista)

class Usuario:
    def __init__(self, id:int, nome:str, email:str):
        self.id = id
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"seu id: {self.id}, nome: {self.nome}, email: {self.email}"
    
#print(listaU)

def buscar_usuario(lista:list, id:int):   
        for usuario in lista:
            if usuario["id"] == id:
                return(f"o seu usuário é o {usuario["nome"]}")
        raise ValueError("Usuário não encontrado")

def transformar_json(lista:list):
    usuarios_json = json.dumps(lista)
    usuarios_objeto = json.loads(usuarios_json)
    return usuarios_json, usuarios_objeto