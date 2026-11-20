from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, turno):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.turno = turno

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Turno: {self.turno}")

    def autenticar(self, senha_informada):
        return senha_informada == self.senha