"""
Cuidados com dados mutaveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor da memoria (mutavel)
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]

lista_b = lista_a
lista_c = lista_a.copy()

lista_a[0]= 'Qualquer coisa'
print(lista_b)
print(lista_c)