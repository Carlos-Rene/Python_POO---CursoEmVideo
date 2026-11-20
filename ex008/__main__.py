from Personagem import *

def main():
    
    p1 = Guerreiro("Kratos", 1000)
    p2 = Mago("Merlin", 2000)

    p1.atacar(p2, 200)
    p1.atacar(p2, 100)
    p2.atacar(p1, 2000)
    p1.status_jogo()

if __name__ == "__main__":
    main()
    