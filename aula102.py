# Try e except

try:
    a = 18
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print('Dividido por zero')
except NameError:
    print('Nome nao esta definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('ACABOU')