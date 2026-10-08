def criar_usuario(lista:list):
    id = lista[-1]["id"] + 1 if lista else 1
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    formulario = {
        "id":id,
        "nome":nome,
        "email":email
    }
    lista.append(formulario)
    return lista

def buscar_usuario(lista:list):
    id = int(input("digite o id que deseja procurar: "))
    for usuario in lista:
        if usuario["id"] == id:
            print(f"seu usuario é o: {usuario}")
            return
    raise ValueError("usuário não encontrado")

def listar_usuario(lista):
    print(f"os usuarios que temos cadastrados são: {lista}")

def atualizar_usuario(lista):
    id = int(input("Digite o id do usuario que deseja alterar: "))
    for usuario in lista:
        if usuario["id"] == id:
            opção = input(f"o usuário encontrado é o {usuario["nome"]} digite o que deseja alterar: nome/email: ")
            if opção == "nome":
                nome = input("digite o novo nome: ")
                usuario["nome"] = nome
                return usuario
            if opção == "email":
                email = input("digite o novo email: ")
                usuario["email"] = email
                return usuario
    print("id não encontrado :(")

def deletar_usuario(lista):
    id = int(input("Digite o id do usuario que deseja deletar: "))
    for usuario in lista:
        if usuario["id"] == id:
            lista.remove(usuario)
            return
    print("id não encontrado :(")
opções = 0
lista = []
print("Seja bem vindo")
while opções != 6:
    opções = input("Escolha o que deseja fazer!\n"
    "Criar usuário = 1\n" \
    "Listar usuários = 2\n" \
    "Buscar por id = 3\n" \
    "Atualizar um usuário = 4\n" \
    "Deletar um usuário = 5\n" \
    "Sair = 6\n" \
    "Opção: ")
    if opções == "1":
        criar_usuario(lista)
    if opções == "2":
        listar_usuario(lista)
    if opções == "3":
        buscar_usuario(lista)
    if opções == "4":
        atualizar_usuario(lista)
    if opções == "5":
        deletar_usuario(lista)
    if opções == "6":
        break
