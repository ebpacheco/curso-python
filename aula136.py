# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Eduardo'
p1.sobrenome = 'Pacheco'

print(p1.nome, p1.sobrenome)

p2 = Pessoa()
p2.nome = 'Natany'
p2.sobrenome = 'Ribeiro'

print(p2.nome, p2.sobrenome)