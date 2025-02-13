"""
Interpolacao basica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Eduardo'
preco = 1000.95897643
variavel = '%s, o preco é R$%.2f' %(nome,preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500)) # minusculo
print('O hexadecimal de %d é %08X' % (1500, 1500)) # maiusculo