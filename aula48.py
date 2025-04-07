"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10,20,30,40]
lista[1] = 200
print(lista)

del lista [3]

lista.append(50)
lista.append(60)
print(lista)

lista.pop()
print(lista)

ultimo_valor = lista.pop(0)
print(lista, 'removido:', ultimo_valor)