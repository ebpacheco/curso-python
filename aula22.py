# Operadores logicos
# and (e), or (ou), not (nao)
# and - Todas as condcioes precisam ser verdadeiras.
# Se qualquer valor for considerado falso, 
# a expressao inteira sera avaliada naquele valor.
# Sao considerados falsy = 0    0.0    ''    False
# Tambem existe o tipo None que é usado para representar um nao valor.

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(' ')
print(bool(0))  # falsy = 0
print(bool(0.0)) # falsy = 0.0
print(bool('')) # falsy = ''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if((entrada == 'E' or entrada == 'e') 
   and senha_digitada == senha_permitida):
    print('Entrar')
else:
    print('Sair')