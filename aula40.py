"""Calculadora com while"""

while True:

    numero_1 = input('Digite o primeiro valor: ')
    numero_2 = input('Digite o segundo valor: ')
    numeros_validos = None

    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos numeros sao invalidos.')
        continue

    operador = input('Digite o operador desejado (+ - * /): ')    
    operador_permitido = '+-*/'

    if operador not in operador_permitido:
        print('Operador invalido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('O resultado é:')
    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = ', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = ', numero_1_float - numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} = ', numero_1_float * numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = ', numero_1_float / numero_2_float)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    #print(sair)

    if sair is True:
        break