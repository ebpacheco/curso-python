# Try, except, else e finally

try:
    a = 18
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print('Dividido por zero')
except NameError:
    print('Nome nao esta definido')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:
    print('ERRO DESCONHECIDO')

print('ACABOU')