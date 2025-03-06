"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um numero inteiro: ')

# try:
#     num_inteiro = int(numero)

#     if num_inteiro % 2 == 0:
#         print(f'{num_inteiro} é par')
#     else:
#         print(f'{num_inteiro} é impar')
# except:
#     print('Digite um numero inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horario = input('Digite a hora: ')

# try:
#     hora_inteiro = int(horario)

#     if hora_inteiro >= 00 and hora_inteiro <= 11:
#         print(f'Bom dia são: {hora_inteiro}h')
#     elif hora_inteiro > 11 and hora_inteiro <= 17:
#         print(f'Boa tarde são: {hora_inteiro}h')
#     elif hora_inteiro > 17 and hora_inteiro < 00:
#         print(f'Boa noite são: {hora_inteiro}h')
#     else:
#      print('Nao conheco essa hora.')
# except:
#     print('Digite a hora em numeros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print('Digite mais de uma letra')