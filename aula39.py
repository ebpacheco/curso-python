"""
Iterando strings com while
"""

nome = 'Eduardo Pacheco'
tamanho_nome = len(nome)

novo_nome = ''
tamanho_novo_nome = 0

while tamanho_novo_nome < tamanho_nome:
    letra = nome[tamanho_novo_nome]
    novo_nome += f'*{letra}'
    tamanho_novo_nome += 1

novo_nome += '*'
print(f'{novo_nome}')
