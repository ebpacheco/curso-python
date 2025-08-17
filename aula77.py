"""
Exercicio
Crie funcoes que duplicam, triplicam e quadruplicam
o numero recebido como parametro
"""

def duplicar(numero):
    return numero*2

def triplicar(numero):
    return numero*3

def quadruplicar(numero):
    return numero*4

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

v_duplicar = criar_multiplicador(2)
v_triplicar = criar_multiplicador(3)
v_quadruplicar = criar_multiplicador(4)
print(v_duplicar(2))
