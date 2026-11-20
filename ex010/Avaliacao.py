class Avaliacao():
    
    def __init__(self, nome, materia, _nota = 0):
        self.nome = nome
        self.materia = materia
        self._nota = _nota

    #metodos acessores
    def get_nota(self):
        return self._nota

    def set_nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida")
        