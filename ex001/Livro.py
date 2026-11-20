from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.progresso_paginas = 1 #estado inicial
        self.finalizado = False #estado novo
        
        print(f"[blue] Você acabou de abrir o livro '[/][red]{self.titulo}[/][blue]' que tem [/][green]{self.paginas} páginas[/] [blue]no total. Agora você está na[/] [yellow]página {self.progresso_paginas}[/]")

    def avancar_paginas(self, numero_paginas):
        avancadas = 0
        
        if self.finalizado:
            print(f'Você já terminou')

        for _ in range(numero_paginas):
            if self.progresso_paginas >= self.paginas:
                 #vai resetar o numero de progressos e nao deixar imprimir mais mensagens
                break

            self.progresso_paginas += 1
            avancadas += 1
            print(f'Pág{self.progresso_paginas} >', end=' ')
            
        if avancadas != 0:
            print(
                f'[blue]Você avançou {avancadas} páginas '
                f'e agora está na[/] [yellow]página {self.progresso_paginas}[/]'
            )
            
        if self.progresso_paginas == self.paginas and not self.finalizado:
            self.finalizado = True
            print(f':monkey_face: [red]Você chegou ao final do livro "{self.titulo}"')

l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5) #self.progresso_página == 6
l1.avancar_paginas(10) #self.progresso_página == 16
l1.avancar_paginas(50) #self.progresso_página == 20
l1.avancar_paginas(1)
