def desafio1():
    #nome = input("Digite seu nome: ")
    #idade = int(input("Digite sua idade: "))

    #print(f"Olá {nome}, você tem {idade}, anos")

    lista = []
    pessoa1= {
        "id":1,
        "nome":"Carlão",
        "email":"carlão@gmail"
    }
    pessoa2 = {
            "id":2,
            "nome":"Robertão",
            "email":"robertão@gmail"
    }
    pessoa3 = {
            "id":3,
            "nome":"Valéria",
            "email":"valéria@gmail"
    }
    
    lista.append(pessoa1)
    lista.append(pessoa2)
    lista.append(pessoa3)
    for pessoa in lista:
        print(pessoa["nome"])
    return lista


def buscarUsuário(lista, id):
    resposta = int(input("digite o id desejado: "))
    for pessoa in lista:
        if resposta == pessoa["id"]:
            print(f"seu usuário é o {pessoa['nome']}")
            return pessoa
    raise ValueError("Não há nenhum usuário com este id")

#lista = desafio1()

#buscarUsuário(lista, id)

class usuario:
    def __init__(self, id:int, nome:str, email:str):
        self.id = id
        self.nome = nome
        self.email = email
        self.lista = []
    def criarUsuário(self):
        usuario1 = usuario(1, "roberto", "roberto@gmail.com")
        usuario2 = usuario(2, "ronaldo", "ronaldo@gmail.com")
        usuario3 = usuario(3, "rodinei", "rodinei@gmail.com")
        self.lista.append(usuario1)
        self.lista.append(usuario2)
        self.lista.append(usuario3)
    def __repr__(self):
        print(self.lista)

usuario.__repr__(self)