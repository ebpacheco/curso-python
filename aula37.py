"""
Repeticoes
while(enquato)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""

contador = 0

while contador < 20:
    contador +=1

    if contador == 5:
     print('Nao vou mostrar o 5')
     continue

    if contador >= 11 and contador <= 15:
     print(f'Nao vou mostrar o {contador}')
     continue

    print(contador)