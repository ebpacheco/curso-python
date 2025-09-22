# Manipulando chaves e valores em Dict

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Eduardo'
pessoa['sobrenome'] = 'Pacheco'

print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Natany'
print(pessoa[chave])

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Nao existe')
else:
    print('Existe')