#Desempacotamento em camadas
#de metodos e funcoes

string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)],  # 2
]

# p, *_, u,  = lista
# print (p,u)

# for nome in lista:
#     print(nome, end=' ', sep='')

# print ('Maria', 'Helena', 1,2,3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

# print(salas)
# print(*salas)
print(*salas, sep='\n')