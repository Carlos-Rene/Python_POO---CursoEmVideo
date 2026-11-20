class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def bonificar(self):
        self.salario = self.salario * 1.1

        return self.salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}; Cpf: {self.cpf}; Salário: {self.salario:.2f}")

