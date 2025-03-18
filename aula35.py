"""
Repeticoes
while(enquato)
Executa uma acao enquanto uma condicao for verdadeira
"""

condicao = True

while condicao:
    nome = input('Digite o seu nome: ')
    print(f'Seu nome é: {nome}')

    if nome == 'sair':
        break

print('Acabou')