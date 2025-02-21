"""
Introducao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero que voce digitar: ')

try:
    print(numero_str)
    numero_float = float(numero_str)
    print(numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.1f}')
except:
    print('Digite um numero valido.')


# if numero_str.isdigit():
#     print(numero_str)
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.1f}')
# else:
#     print('Digite um numero valido.')