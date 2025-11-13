#Introducao as Generator functions em Python

def generator(n=0, maximum=10):
    while True:
        yield n
        if n >= maximum:
            return
        n+=1
        
gen = generator(maximum=100)

for n in gen:
    print(n)