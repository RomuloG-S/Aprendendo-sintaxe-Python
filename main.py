import json
from service import buscar_usuario, adicionar_usuario

if __name__ == "__main__":
    lista = []
    adicionar_usuario(lista, 1, "romulo", "romulo@gmail.com")
    adicionar_usuario(lista, 2, "pedro", "pedro@gmail.com")
    adicionar_usuario(lista, 3, "alex", "alex@gmail.com")

    print(lista)

    try:
        buscar_usuario(lista, 4)
    except ValueError:
        print("esse id é inexistente")