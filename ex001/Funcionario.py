from rich import print
from rich import inspect

class Funcionario:
    #Atributo de classe
    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        #Atributo de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    #declaraçao dos metodos de instancia
    def apresentacao(self) -> str:
        return f':monkey_face: Olá, sou [yellow]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}.'


f1 = Funcionario('Maria', 'Administração', 'Diretora')
print(f1.apresentacao())
inspect(f1, methods=True)
inspect(Funcionario)


f2 = Funcionario('Pedro', 'TI', 'Programador')
print(f2.apresentacao())