#Problema dos parametros mutavies em funcoes Python

def adicionar_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adicionar_clientes('Eduardo')
adicionar_clientes('Natany', cliente1)
cliente1.append('Rita')

cliente2 = adicionar_clientes('Silvia')
adicionar_clientes('Duda', cliente2)

cliente3 = adicionar_clientes('Rafaela')
adicionar_clientes('Babi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)