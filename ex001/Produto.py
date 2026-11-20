from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco = 0): #metodo construtor
        self.nome = nome
        self.preco = preco

    #criaçao da etiqueta / metodo de instancia
    def etiqueta(self):
        conteudo = f'{self.nome.center(30, " ")}'
        conteudo += '-' * 30
        precof = f'{self.preco:,.2f}'
        conteudo += precof.center(30, '.')

        painel = Panel(renderable= conteudo, title='Produto', width=34)

        print(painel)

p1 = Produto('Iphone 17 Pro Max', 8_000)
p1.etiqueta()