"""
Fatiamento de strings
 012345678
 Ola mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a funcao len retorna a qtd de caracteres da str
"""
variavel = 'Ola mundo'
print(variavel[-4]) #u
print(variavel[4:8]) #mund
print(variavel[4:]) #mundo
print(variavel[0:5]) #Ola m
print(variavel[:5]) #Ola m
print(variavel[-8:-3]) #la mu
print(variavel[3]) # 
print(len(variavel[3])) # 1
print(len(variavel)) # 9
print(variavel[0:len(variavel):1]) #Ola mundo
print(variavel[0:9:1]) #Ola mundo
print(variavel[0:9:2]) #Oamno
print(variavel[0:9:3]) #O n  
print(variavel[::-1]) #odnum alO
print(variavel[-1:-10:-1]) #odnum alO
