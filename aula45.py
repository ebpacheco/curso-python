"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""

# texto1 = 'Eduardo'.__iter__
# texto1 = iter('Eduardo') #__iter__()

# print(next(texto1))
# print(next(texto1))
# print(next(texto1))
# print(next(texto1))
# print(next(texto1))
# print(next(texto1))
# print(next(texto1))
# print(next(texto1)) #Erro 

# print(texto1.__next__())
# print(texto1.__next__())
# print(texto1.__next__())
# print(texto1.__next__())
# print(texto1.__next__())
# print(texto1.__next__())
# print(texto1.__next__())
# print(texto1.__next__()) #Erro

texto2 = 'Pacheco'
iterator = iter(texto2)
print(iterator)

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break

for letra in texto2:
    print(letra)