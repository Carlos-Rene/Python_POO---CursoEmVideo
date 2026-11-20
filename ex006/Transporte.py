from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = self.calcular_frete()
        

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):

    fator = 0.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        return f"R${self.distancia * self.fator:.2f}"


class Caminhao(Transporte):

    fator = 1.2

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia >= 50:
            return f"R${self.distancia * self.fator:.2f}"

        return f"Raio mínimo de 50km"


class Drone(Transporte):
    
    fator = 9.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia <= 10:
            return f"R${self.distancia * self.fator:.2f}"

        return f"Raio máximo de 10km"