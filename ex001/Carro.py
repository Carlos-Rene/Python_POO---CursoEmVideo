#declaração classe
class Carro:
    def __init__(self, marca, ano): #método construtor
        #atributos de instancia
        self.marca = marca
        self.ano = ano
        self.velocidade = 0

    #metodos de instancia

    def acelerar(self, valor):
        self.velocidade += valor

        return self.velocidade
    
    def frear(self, valor):
        # acelerar(70) > frear(20)
        if self.velocidade >= valor:
            self.velocidade -= valor
            
            return self.velocidade
        else:
            self.velocidade = 0

            return self.velocidade

    def mensagem(self):
        print(f'\nCarro da marca: {self.marca}')
        print(f'Do ano de: {self.ano}')
        print(f'Velocidade: {self.velocidade}Km')
        
        multa = self.multa()

        if multa != 0:
            print(f'Recebe uma multa R$ {multa}')        
        else:
            print('O condutor não recebe multa')

    def multa(self):
        preco_multa = 0

        if 60 < self.velocidade < 100:
            preco_multa = 188.89
            return preco_multa
        
        elif self.velocidade > 100:
            preco_multa = 888.89

        return preco_multa


print('AVENIDA - MÁX DE 60KM\n')

#declaração da instância
carro = Carro(
    str(input('Marca do carro: ')),
    int(input('Ano do carro: ')),
)

acelerar = carro.acelerar(90)
frear = carro.frear(20)
carro.mensagem()

