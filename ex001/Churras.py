from rich.panel import Panel
from rich import print
from rich import inspect

class Churrasco:
    kg = 0.4 #cada pessoa come em média 400g de carne
    precoKG = 82.40 #preço de cada Kg de carne

    def __init__(self, titulo = '', quant = 0):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n'
        conteudo += f'Cada participante comerá {self.kg}Kg e cada kg custa R${self.precoKG:.2f}\n'
        conteudo += f'Recomendo [blue]comprar {self.quantKg():.3f}Kg[/] de carne\n'
        conteudo += f'O custo total será de [green]R${self.custoTotal():.2f}[/]\n'
        conteudo += f'Cada pessoa vai pagar [yellow]R${self.precoPessoa():.2f}[/]'

        tabela = Panel(conteudo, title=self.titulo, width=70)

        print(tabela)

    def quantKg(self):
        totalKg = self.kg * self.quant
        
        return totalKg
    
    def custoTotal(self):
        custoKgTot = self.quantKg() * self.precoKG
        
        return custoKgTot
    
    def precoPessoa(self):
        if self.quant == 0:
            return 0

        return self.custoTotal() / self.quant



c1 = Churrasco('Churras dos amigos', 15)
c1.analisar()
