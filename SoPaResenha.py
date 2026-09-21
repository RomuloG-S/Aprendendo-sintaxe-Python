from dataclasses import dataclass
class Carro:
    def __init__(self, modelo:str, ano:int, marca:str, quilometragem:int, valor:int):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.quilometragem = quilometragem
        self.valor = valor
        self.desconto = self.CalcularDesconto()

    def ExibirInfos(self):
        return (f"O Modelo deste carro é um {self.modelo}, do ano de {self.ano}, da marca {self.marca},"
                f" com apenas {self.quilometragem} de quilometragem, no valor amigável de {self.valor} R$")

    def CalcularDesconto(self):
        anoA = 2026
        desconto = self.valor
        while self.ano < anoA:
            desconto = desconto - (desconto * 0.05)
            anoA -= 1
        return round(desconto)

    def UsadoOuNovo(self):
        if self.quilometragem == 0:
            print("Este carro é novo")
        elif 0 < self.quilometragem < 10000:
            print("Este carro é semi novo")
        elif self.quilometragem > 10000:
            print("Este carro é usado")



carro1 = Carro("civic", 2020,"honda", 200000,50000)

# print(round(Carro.CalcularDesconto(carro1)))

class Concessionaria:
    def __init__(self):
        self.carros = []

    def CriarCarro(self):
        modelo = input("Fale o modelo do carro: ")
        ano = int(input("Fale o ano do carro: "))
        marca = input("Fale a marca do carro: ")
        quilometragem = int(input("Fale a quilometragem do carro: "))
        valor = int(input("Qual a fipe do carro: "))

        carro = Carro(modelo, ano, marca, quilometragem, valor)

        self.carros.append(carro)
        print("Carro Cadastrado")

    def ListarCarro(self):
        print('Os carros no pátio atualmente são: ')
        for carro in self.carros:
            print(carro.modelo)

    def ProcurarCarro(self):
        pesquisa = input("Somos uma concessionária que vende carros da honda e nissan"
                         "caso queira carros nissan, Digite: Nissan"
                         "caso queira carros honda, Digite: Honda")

        if pesquisa == "Honda":
            print(f'Os carros da honda são')
            for carro in self.carros:
                if carro.marca == "Honda":
                    print(carro.modelo)
        elif pesquisa == "Nissan":
            print(f'Os carros da nissan são')
            for carro in self.carros:
                if carro.marca == "Nissan":
                    print(carro.modelo)
        else:
            print("digite uma opção válida")

    def ValorDoPátio(self):
        valor_total = 0

        for carro in self.carros:
            valor_total += carro.desconto
        print(f"O valor total do pátio no momento é: {valor_total}")


def main():
    escolha = ""
    loja = Concessionaria()
    print("Bem vindo a concessionária Honissan")
    while escolha != "5":
        print("Na honinssan você pode solicitar as seguintes coisas:\n"
          "Adicionar Carro(1),\n"
          "Listar carros(2),\n"
          "Procurar Carro Especifico(3),\n"
          "Valor total de carros(4),\n"
          "Sair(5)")
        escolha = input("O que você deseja fazer: ")
        match escolha:
            case "1":
                loja.CriarCarro()
            case "2":
                loja.ListarCarro()
            case "3":
                loja.ProcurarCarro()
            case "4":
                loja.ValorDoPátio()
            case "5":
                print("Tenha um ótimo dia!")
            case _:
                print("Opção inválida")

if __name__ == "__main__":
    main()