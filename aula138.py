#Metodos em instancias de classes Python
#Hard Coded - É algo que foi escrito diretamento no codigo

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} esta acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

palio = Carro('Palinho')
print(palio.nome)
palio.acelerar()

string = 'Eduardo'
print(string.upper())