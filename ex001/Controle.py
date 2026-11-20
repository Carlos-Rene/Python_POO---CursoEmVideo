from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 5
     
    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    #metodos do objeto
    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1
                
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_max:
                pass
            else:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_min:
                pass
            else:
                self.volume_atual -= 1

    def mostrar_tv(self):
        conteudo = ''

        if not self.ligado:
            conteudo = f':prohibited:[red] A TV está desligada[/red]'
        else:
            conteudo = f'CANAL  = '

            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f'[green on red] {canal} [/]'
                else:
                    conteudo += f' {canal} '

        conteudo += f'\nVOLUME = '

        for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
            if volume <= self.volume_atual:
                conteudo += f'[black on cyan] [/]'
            else:
                conteudo += f'[black on white] [/]'

        tv = Panel(conteudo, width=35, height=4, title='[ TV ]')
        print(tv)


c = ControleRemoto(volume=1)

while True:
    c.mostrar_tv()
    comando = str(input(f"< CH{c.canal_atual} >  - VOL{c.volume_atual} + "))

    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '<':
            c.canal_menos()
        case '>':
            c.canal_mais()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()
    print('\n' * 10)