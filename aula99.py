import sys

#Generator expression, Iterables e Iteratos em Python

iterable=['Eu', 'Tenho', '__iter__']
iterator= iter(iterable)
lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

for n in generator:
    print(n)