"""
Exercicios com funcoes

Crie uma funcao que multiplica todos os argumentos
nao nomeados recebidos
Retorne o total para uma variavel e mostre o valor 
da variavel

Crie uma funcao que fala se um numero é par ou impar
Retorne se o numero é par ou impar
"""

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

valor = multiplicar(1,2,3,4,5)
print(valor)

#
def par_impar(numero):
    if numero % 2 == 0:
        return(f'O numero {numero} é par')
    #else:
    return(f'O numero {numero} é impar')

numero = par_impar(2)
print(numero)
