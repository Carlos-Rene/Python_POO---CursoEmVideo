from rich import print

class Caneta:
    def __init__(self, cor = 'azul'):
        escolha = ''

        match cor.lower().strip(): 
            case 'azul':
                escolha = '[blue]'
            case 'verde':
                escolha = '[green]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'amarelo':
                escolha = '[yellow]'
            case _:
                escolha = '[white]'

        self.cor = escolha
        self.tampada = True

    def destampar(self):
        self.tampada = False

        return self.tampada
    
    def tampar(self):
        self.tampada = True

        return self.tampada

    def escrever(self, frase):
        if self.tampada:
            print(f'A {self.cor}caneta[/] está tampada!')

        print(f'{self.cor}{frase}[/]', end=' ')

    def quebrarLinha(self, valor = 0):
        print('\n' * valor)


#objetos de instancia
c1 = Caneta('verde')
c2 = Caneta('vermelho')
c3 = Caneta('azul')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, mundo!')
c1.quebrarLinha(1)
c2.escrever('POO é mt bom!')
c3.escrever('Vamos exercitar!')