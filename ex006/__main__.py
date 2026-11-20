from Transporte import *
from rich import print
from rich.table import Table


def main():
    dist = 20

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for c in range(len(viagem)):
        tabela.add_row(f"{str(dist)}Km", type(viagem[c]).__name__, str(viagem[c].frete))

    print(tabela)

if __name__ == "__main__":
    main()