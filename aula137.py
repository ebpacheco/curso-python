# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Eduardo', 'Pacheco')
# p1.nome = 'Eduardo'
# p1.sobrenome = 'Pacheco'

print(p1.nome, p1.sobrenome)

p2 = Pessoa('Natany', 'Ribeiro')
# p2.nome = 'Natany'
# p2.sobrenome = 'Ribeiro'

print(p2.nome, p2.sobrenome)