from Termostato import Termostato
from rich import print, inspect


def main():
    t = Termostato()
    try:
        t.temperatura = 25.2
        print(t.ftemperatura)
    except Exception as error:
        print(f"Houve um erro. A temperatura de {error} é inválida")    

if __name__ == "__main__":
    main()