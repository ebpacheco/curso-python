# Variáveis livres + nonlocal (locals, globals)
def concatenar(string_inicial):

    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
         nonlocal valor_final # UnboundLocalError
         valor_final += valor_a_concatenar
         return valor_final

    return interna


concat = concatenar('a')
print(concat('b'))