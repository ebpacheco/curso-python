"""
Higher Order Functions
Funcoes de primeira classe
""" 

def saudacoes(msg, nome):
    return (f'{msg}, {nome} !') 

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacoes, 'Bom dia', 'Eduardo')
#variavel = saudacoes('Bom dia', 'Eduardo')
print(v)