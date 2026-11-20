from abc import ABC, abstractmethod
from random import randint, choice
from rich import print
from rich.table import Table


class Personagem(ABC):

    def __init__(self, nome, vida = 0, golpes = None):
        self.nome = nome
        self.vida = vida
        self.golpes = [] or golpes
        self.golpes_usados = tuple()

    def atacar(self, alvo, forca):
        if self.vida > 0 and alvo.vida > 0:
            #escolher um golpe aleatorio
            golpe = choice(self.golpes)

            #golpes usados para mostrar no "status_jogo"
            self.golpes_usados += (golpe, )

            #dano aleatorio com o minimo de 1 ate o max de "forca"
            dano = randint(1, forca)
            
            print(
                    f"[green]{self.nome}[/]({self.vida}) "
                    f"atacou [red]{alvo.nome}[/]({alvo.vida}) "
                    f"com um [yellow]{golpe}[/] de força {forca}"
                    )
            
            #vai poder atacar
            alvo.receber_dano(dano)

    def receber_dano(self, dano):
        #o objeto diminui a vida
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

        print(f"[red]{self.nome} recebeu {dano} de dano[/]!")

    def status_jogo(self):
        status = Table(title="Status do Personagem")

        status.add_column("Nome")
        status.add_column("Vida")
        status.add_column("Golpes Utilizados")
        status.add_row(self.nome, str(self.vida), ", ".join(self.golpes_usados))

        print(status)

    @abstractmethod
    def curar(self):
        #pode curar de 1 a 100 pontos, de acordo com o dado lançado (numero random)
        pass


class Guerreiro(Personagem):

    def __init__(self, nome = "", vida = 0):
        super().__init__(
            nome, 
            vida,
            ["Soco", "Pulo Giratório", "Golpe de Machado"]
        )
        
    def curar(self):
        #curar o personagem e imprimir na tela quanto de vida curou
        cura = randint(1, 100)
        self.vida += cura

        print(
            f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e "
            f"[green]recuperou {cura} pontos[/] de vida."
        )


class Mago(Personagem):

    def __init__(self, nome = "", vida = 0):
        super().__init__(
            nome,
            vida,
            ["Bola de Fogo", "Raio de Gelo", "Relâmpago"]
        )
        
    def curar(self):
        cura = randint(1, 100)
        self.vida += cura

        print(
            f"[blue]{self.nome}[/] fez uma magia de cura nos ferimentos "
            f"e [green]recuperou {cura} pontos[/] de vida."
        )


class Lanceiro(Personagem):
    
    def __init__(self, nome, vida = 0):
        super().__init__(
            nome,
            vida,
            ["Perfura-Coração", "Impulso de Falange", "Estocada Linear"]
        )
        
    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        
        print(
            f"[blue]{self.nome}[/] fez enroulou uma atadura nos ferimentos "
            f"e [green]recuperou {cura} pontos[/] de vida."
        )        