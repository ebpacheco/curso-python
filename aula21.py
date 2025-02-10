# Operadores logicos
# and (e), or (ou), not (nao)
# and - Todas as condcioes precisam ser verdadeiras.
# Se qualquer valor for considerado falso, 
# a expressao inteira sera avaliada naquele valor.
# Sao considerados falsy = 0    0.0    ''    False
# Tambem existe o tipo None que é usado para representar um nao valor.

print(True and True)
print(True and False)
print(False and True)
print(False and False)

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if(entrada == 'E' and senha_digitada == senha_permitida):
    print('Entrar')
else:
    print('Sair')
