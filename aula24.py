# Operadores in e not in
# Stings sao iteraveis
# 0 1 2 3 4 5 6
# E d u a r d o
#-7-6-5-4-3-2-1

nome = 'Eduardo'
print(nome[0]) # E
print(nome[1]) # d
print(nome[2]) # u
print(nome[3]) # a
print(nome[4]) # r
print(nome[5]) # d
print(nome[6]) # o

print(nome[-7]) # E
print(nome[-6]) # d
print(nome[-5]) # u
print(nome[-4]) # a
print(nome[-3]) # r
print(nome[-2]) # d
print(nome[-1]) # o

print('E' in nome) # True
print('Z' in nome) # False
print('ardo' in nome) # True
print('nan' in nome) # False
print(10 * '-')
print('E' not in nome) # True
print('Z' not in nome) # False
print('ardo' not in nome) # False
print('nan' not in nome) # True
print(10 * '-')

nome_digitado = input ('Digite seu nome: ')
encontrar = input ('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
     print(f'{encontrar} nao esta em {nome}')