"""
Closure e funcoes que retornam outras funcoes
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return (f'{saudacao}, {nome}!')
    return saudar

#criar_saudacao(saudacao)
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nomes in ['Eduardo', 'Natany', 'Rita']:
    #saudar(nome)
    print(falar_bom_dia(nomes))

