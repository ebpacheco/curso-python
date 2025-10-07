# Empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a 
# print(a,b)

pessoa = {
    'nome': 'Eduardo',
    'sobrenome': 'Pacheco'
}

# a,b = pessoa
# print(a, b)

# c, d = pessoa.values()
# print(c, d)

# e, f = pessoa.items()
# print(e, f)

# (e1,e2), (f1,f2) = pessoa.items()
# print(e1, e2)
# print(f1, f2)

# for chave, valor in pessoa.items():
#     print(chave, valor)


# args e kwargs
# args (já vimos)

pessoa = {
    'nome': 'Eduardo',
    'sobrenome': 'Pacheco',
}

dados_pessoa = {
    'idade': 32,
    'altura': 1.8,
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)


# kwargs - keyword arguments (argumentos nomeados) 

def mostra_argumento_nomeados(*args, **kwargs):
    print('NAO NOMEADOS:', args)
    
    for chave, valor in kwargs.items():
        print(chave,valor)

mostra_argumento_nomeados(1,2, nome='Eduardo', qlq=123)
print()
mostra_argumento_nomeados(**pessoas_completa)