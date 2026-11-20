class Avaliacao():
    
    def __init__(self, nome, materia, _nota = 0):
        self.nome = nome
        self.materia = materia
        self._nota = _nota

    #Criando atributo validável
    @property
    def nota(self): #getter
        return self._nota

    @nota.setter
    def nota(self, valor):
            if 0 <= valor <= 10:
                self._nota = valor
            else:
                print("Nota inválida")
      