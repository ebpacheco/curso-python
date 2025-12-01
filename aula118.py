# count é um iterador sem fim (itertools)

from itertools import count

c1 = count(50, step=5)
r1 = range(50, 100, 5)

print('Count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()

print('Range')
for i in r1:
    print(i)