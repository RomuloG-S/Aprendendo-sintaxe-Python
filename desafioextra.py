notas = [10, 20, 10, 30]
def calcular_media(notas:list) -> float:
    soma = 0.0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media

medias = calcular_media(notas)

def adicionar_usuario()

