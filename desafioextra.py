notas = [10, 20, 10, 30]
def calcular_media(notas:list) -> float:
    soma = 0.0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media

medias = calcular_media(notas)
lista = []

def adicionar_usuario(lista:list, id:int, nome:str, email:str) -> list:
    formulario = {
        "id":id,
        "nome":nome,
        "email":email
    }
    lista.append(formulario)
    return lista

adicionar_usuario(lista, 1, "Pedro", "pedro@gmail.com")
adicionar_usuario(lista, 2, "Paulo", "paulo@gmail.com")
adicionar_usuario(lista, 3, "Alex", "alex@gmail.com")

#print(lista)

class Usuario:
    def __init__(self, id:int, nome:str, email:str):
        self.id = id
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"seu id: {self.id}, nome: {self.nome}, email: {self.email}"
    
listaU = [
Usuario(1, "Pedro", "pedro@gmail.com"),
Usuario(2, "Paulo", "paulo@gmail.com"),
Usuario(3, "Alex", "alex@gmail.com")
]

#print(listaU)

def buscar_usuario(lista:list, id:int):   
        for usuario in lista:
            if usuario.id == id:
                return usuario
        raise ValueError("Usuário não encontrado")

try:
    print("existe o id e ele é", buscar_usuario(listaU, 1))
except ValueError:
    print("Não existe esse usuário")

