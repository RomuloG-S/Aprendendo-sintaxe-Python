import json
from service import buscar_usuario, adicionar_usuario, criar_arquivo, transformar_json, ler_arquivo

if __name__ == "__main__":
    lista = []
    adicionar_usuario(lista, 1, "romulo", "romulo@gmail.com")
    adicionar_usuario(lista, 2, "pedro", "pedro@gmail.com")
    adicionar_usuario(lista, 3, "alex", "alex@gmail.com")
    #json_texto, objeto, foi criado para transformar os dados da lista em uma string,
    # pois o python não consegue receber alem de str
    json_texto, objeto = transformar_json(lista)
    
    criar_arquivo(json_texto)
    dados_do_json = ler_arquivo(json_texto)
    print(dados_do_json[0]["nome"])
    

    
#    try:
#        buscar_usuario(lista, 4)
#    except ValueError:
#        print("esse id é inexistente")