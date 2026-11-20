from Avaliacao import *
from rich import print, inspect


def main():

    av1 = Avaliacao("Pedro", "Matemática")
    av1.nota = -4
    #inspect(av1, private=True)
    print(f"O aluno {av1.nome} tirou {av1.nota} em {av1.materia}")

if __name__ == "__main__":
    main()