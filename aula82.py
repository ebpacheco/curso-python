# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Eduardo',
    'sobrenome': 'Pacheco'
}

# print(p1['nome'])
# print(p1.get('nome', None))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'Natany',
#     'idade': 35
# })

# p1.update(nome='Rita', idade=5)

# tupla = (('nome', 'novo valor tupla'),('idade', 99))
# p1.update(tupla)

lista = [['nome', 'novo valor lista'],['idade', 88]]
p1.update(lista)

print(p1)
