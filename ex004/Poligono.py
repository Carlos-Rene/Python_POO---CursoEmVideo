from abc import ABC, abstractmethod
PI = 3.14

class Poligono(ABC):

    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return (self.qtd_lados * self.lado)

    def area(self):
        return (self.lado ** 2)    


class Circulo(Poligono):
    
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * PI * self.raio

    def area(self):
        return PI * (self.raio ** 2)