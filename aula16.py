# if / elif / else
# se / se nao se / se nao

entrada = input('Voce quer "entrar" ou "sair"? ')
entrada.lower
if entrada == "entrar":
    print('Voce entrou no sistema')
    print(123)
elif entrada == "sair":
    print('Voce saiu do sistema')
else:
    print('Voce nao digitou nem entrar e nem sair')
print('FORA DOS BLOCOS')