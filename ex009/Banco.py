class ContaBancaria:
    def __init__(self, id, nome, __saldo = 0):
        self.id = id
        self._titular = nome
        self.__saldo = __saldo
        self.valores = list()
        print(f"Conta {id} criada com sucesso. Saldo atual R${__saldo}")

    def __str__(self):
        #return f"A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo"
        return f"Estado atual da conta {self.__dict__}"
    
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor

        print(f"Depósito de {valor} autorizado na conta {self.id}")
        
    def sacar(self, valor = 0):
        if self.__saldo >= valor:
            self.__saldo -= valor
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
        print(f'Saldo atualizado: R${self.__saldo}')     
