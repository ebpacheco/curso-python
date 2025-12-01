# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(lista):
    print(*list(lista), sep='\n')
    print()

pessoas = ['Joao', 'Joana', 'Luiz', 'Leticia']

# print_iter(combinations(pessoas,2))
# print_iter(permutations(pessoas,2))

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masc', 'fem']
]

print_iter(product(camisetas))
print_iter(product(*camisetas))