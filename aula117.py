"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

# print(lista_index)

def soma(lista1, lista2):
    lista_index = min(len(lista1),len(lista2))
    return [(l1[i] + l2[i]) for i 
            in range(lista_index)]

print(soma(l1,l2))


#Solucao que funciona em todas as linguagens
lista_soma = []
for i in range(len(l2)):
    lista_soma.append(l1[i] + l2[i])
print(lista_soma)

#Solucao com funcao python
lista_soma2 = [x+y for x,y in zip(l1,l2)]
print(lista_soma2)