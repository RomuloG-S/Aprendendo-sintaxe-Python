def desafio1():
    lista = []

    usuário1 = {
        "id":1,
        "nome":"pedro",
        "email":"pedro@gmail.com"
    }

    usuário2 = {
        "id":2,
        "nome":"paulo",
        "email":"paulo@gmail.com"
    }

    usuário3 = {
        "id":3,
        "nome":"alex",
        "email":"alex@gmail.com"
    }

    lista.append(usuário1)
    lista.append(usuário2)
    lista.append(usuário3)

    #for usuario in lista:
        #print(usuario["nome"])

    return lista

def buscaUsuario(lista):
    resposta = int(input("Digite o id desejado: "))
    usuarioEncontrado = False
    for pessoa in lista:
        if resposta == pessoa["id"]:
            usuarioEncontrado = True
            print(f"O usuário com este id é: {pessoa["nome"]}")
    if not usuarioEncontrado:
        print("none")
        

lista = desafio1()
listaU = []
class Usuario:
    def __init__(self, id:int = None, nome:str = None, email:str = None):
        self.id = id
        self.nome = nome
        self.email = email
    def CriarUsuario(self):
        resposta = ''
        while resposta == "":    
            self.id = int(input("digite o id do usuário: "))
            self.nome = input("digite o nome do usuário: ")
            self.email = input("digite o email do usuário: ")
            resposta = input("se quiser continuar pressione enter, caso contrario digite qualquer coisa: ")
            usuario = Usuario(self.id, self.nome, self.email)
            listaU.append(usuario)
            if resposta != "":
                break
    def __repr__(self):
        usuarios_str = "\n".join([f"{u.id}, {u.nome}, {u.email}" for u in listaU])
        return f"Os usuários que temos são:\n{usuarios_str}"

usuarios = Usuario()
usuarios.CriarUsuario()
print(usuarios)