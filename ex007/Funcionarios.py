from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):

    salario_minimo = 1_612
    desconto_inss = 7.5

    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        mensagem = (
            f"O salário de [blue]{self.nome}[/] [red]({type(self).__name__})[/] "
            f"é de [green]R${self.salario:.2f}[/] e corresponde a "
            f"[yellow]{self.salario / self.salario_minimo:.1f} salários mínimos.[/] "
        )

        painel = Panel(mensagem, title = "Análise de Salário", height=5, width=50)

        print(painel)


class FuncionarioHorista(Funcionario):

    def __init__(self, nome, valor_hora = 0, qtd_horas = 0, sal_bruto = 0):
        super().__init__(nome, sal_bruto)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calcular_salario(self):
        if self.sal_bruto == 0:
            self.sal_bruto = self.qtd_horas * self.valor_hora
            
        self.salario = self.sal_bruto * (1 - self.desconto_inss / 100)


class FuncionarioMensalista(Funcionario):
    
    def __init__(self, nome, sal_bruto = 0):
        super().__init__(nome, sal_bruto)
    
    def calcular_salario(self):
        self.salario = self.sal_bruto * (1 - self.desconto_inss / 100)