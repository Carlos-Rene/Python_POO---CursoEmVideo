from Avaliacao import *
from rich import print, inspect


def main():

    av1 = Avaliacao("Pedro", "Matemática")
    print(av1.get_nota())
    av1.set_nota(7.4)
    inspect(av1, private=True)

if __name__ == "__main__":
    main()