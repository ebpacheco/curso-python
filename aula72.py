"""
Retorno de valores das funcoes (return)
"""

def soma(x,y):
    if x > 10:
        return 10,20
    return x + y

soma1 = soma(2,2)
soma2 = soma(5,5)
soma3 = soma(20, 30)

print(soma1)
print(soma2)
print(soma3)