from pprint import pprint
import copy
# copy, sorted, produtos.sort
# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
pprint(produtos)
print()

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)
novos_produtos = [
    {
        **novos_produtos, 'preco' : novos_produtos['preco'] + 0.10
    } for novos_produtos in novos_produtos
]

pprint(novos_produtos)
print()

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda p: p["nome"])
pprint(produtos_ordenados_por_nome)
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda p: p["preco"])
pprint(produtos_ordenados_por_preco)
print()