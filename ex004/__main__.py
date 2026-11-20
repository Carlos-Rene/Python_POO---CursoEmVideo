from Poligono import *

def main():
    p1 = Quadrado(20)

    print(f"Um {type(p1).__name__} de lado {p1.qtd_lados} tem perímetro de {p1.perimetro():.1f}mm")
    print(f"Um {type(p1).__name__} de lado {p1.qtd_lados} tem uma área de {p1.area():.1f}mm²\n")

    p2 = Circulo(20)
    print(f"Um {type(p2).__name__} de raio {p2.raio} tem perímetro de {p1.perimetro():.1f}mm")
    print(f"Um {type(p2).__name__} de raio {p2.raio} tem uma área de {p1.area():.1f}mm²")

if __name__ == "__main__":
    main()
    