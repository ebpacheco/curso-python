"""
Argumentos nomeados e nao nomeados em funcoes Python
Argumento nomeado tem nome com sinal de igual
Argumento nao nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    #print(x + y + z)
    print(f'{x=} y={y} {z=} |  x + y + z =', x + y + z)

#Argumento nao nomeado
soma(1, 2, 3)

#Argumento nomeado
soma(z=3, x=1, y=2)