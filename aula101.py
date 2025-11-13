# Yield from

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

def gen3(gen):
    yield from gen()
    yield 7
    yield 8
    yield 9

g1 = gen1()
g2 = gen2()
g3 = gen3(gen2)

for n1 in g1:
    print(n1)
print()
for n2 in g2:
    print(n2)
print()
for n3 in g3:
    print(n3)