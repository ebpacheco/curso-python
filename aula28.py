"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Qual o seu nome? ')
idade = input('Qaul sua idade? ')

quantidade_letras = len(nome)
nome_invertido = nome[::-1]
letra_primeria = nome[0]
letra_ultima = nome[quantidade_letras-1] #nome[-1]

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome_invertido}')

    if ' ' in nome:
        print(f'Seu nome {nome} contém espaços')
    else:
        print(f'Seu nome {nome} nao contém espaços')

    print(f'Seu nome tem {quantidade_letras} letras')
    print(f'A primeira letra do seu nome é {letra_primeria}')
    print(f'A última letra do seu nome é {letra_ultima}')
else:
    print(f'"Desculpe, você deixou campos vazios."')