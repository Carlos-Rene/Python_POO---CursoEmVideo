class ContaBancaria:
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        self.valores = list()
    
    def sacar(self, valor = 0):
        if self.saldo >= valor:
            self.saldo -= valor
            self.valores.append(valor)

            print(f'Saque de R${valor} aprovado')
            return True

        print(f'Saque não aprovado.')
        return False

    def extrato_saques(self):
        print(f'Extrato de saques: ', end='')
        for valor in self.valores:
            print(f'R${valor}', end=' ')
        print()

    def mostrar_saldo(self):
        print(f'Saldo atualizado: R${self.saldo}')     


#criaçao do "objeto"
cb1 = ContaBancaria(1, 'Teste', 100)

cb1.sacar(200)
cb1.sacar(50)
cb1.sacar(20)
cb1.extrato_saques()
cb1.mostrar_saldo()