#Escopo de classe e de metodos da classe

class Animal:

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        self.alimento = alimento
        return f'O {self.nome} esta comendo {self.alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal('Leão')
print(leao.nome)

print(leao.comendo('Banana'))
print(leao.executar('Beterraba'))
