"""
args - Argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
"""

#Lembre-te de desempacotamento
x, y, *resto = 1,2,3,4,5,6
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        #print(total, numero)
        total += numero
        #print('Total: ', total)
    #print(total)
    return total

var = soma(1, 2, 3, 4, 5, 6)
print (var)

var1 = soma(1, 2, 3)
print (var1)

var2 = soma(4, 5, 6)
print (var2)

#funcao SUM() faz a soma dos valores
print(sum((4, 5, 6)))

numeros = 1,2,3,4,5,6,7,8,9
#fazendo desempacotamento com *numeros
outra_soma = soma(*numeros)
print(outra_soma)