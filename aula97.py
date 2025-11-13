#dir, hasattr e getatter em Python

string = 'Eduardo'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'existe {metodo}')
    print(getattr(string, metodo)())
else:
    print(f'Nao existe o metodo {metodo}')