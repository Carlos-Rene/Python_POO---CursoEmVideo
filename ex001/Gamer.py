from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = list()

    def add_favoritos(self, jogo):
        if jogo not in self.jogos:
            self.jogos.append(jogo)

    def ficha(self):
        if self.jogos:
            lista = [
                f'Nome real: [bold on red]{self.nome}[/]',
                'Jogos favoritos: '
            ]

            for jogo in self.jogos:
                lista.append(f':monkey_face: [blue]{jogo}[/]')

            conteudo = '\n'.join(lista)
        else:
            conteudo = ''
        
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width=40)

        return painel


j1 = Gamer('Fabrício da Silva', 'detonator2025')
j1.add_favoritos('Fortnite')
j1.add_favoritos('God of War')
print(j1.ficha())



j2 = Gamer('Eliana', 'peach_raivosa')
j2.add_favoritos('Mario Bros')
print(j2.ficha())