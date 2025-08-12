"""
Introducao as funcoes (def) em Python
Funcoes sao trechos de codigo usados para
replicar determinada acao ao longo do seu codigo
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrao, funcoes Python retornam None (nada).
"""

def imprimir():
    print("Varias 1")
    print("Varias 2")
    print("Varias 3")
    print("Varias 4")

imprimir()

def saudacao(nome):
    print(f'Ola, {nome}')

saudacao('Eduardo')
