from Funcionario import Funcionario
from Gerente import Gerente

def main():
    f1 = Funcionario('teste', 1234567, 1000)
    f1.bonificar()
    f1.exibir_dados()

    g1 = Gerente("Helena", 123456, 2000, "123", "Dia")
    senha = str(input("Senha: "))

    print(g1.autenticar(senha))

if __name__ == "__main__":
    main()