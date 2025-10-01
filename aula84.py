# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
s0 = set('Eduardo')
s1 = set()  # vazio
s1 = {'Eduardo', 1, 2, 3}  # com dados
# print(s0)
# print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

l1 = [1,2,3,3,3,3,1]
s1 = set(l1)
# print(s1)
# print(3 in s1)
# print(3 not in s1)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Eduardo')
s1.add(1)
s1.update((1,2,3,'Pacheco'))
# s1.clear()
s1.discard(1)
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença "-" - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2 #união
print(s3)

s4 = s1 & s2 #intersecção
print(s4)

s5 = s1 - s2 #diferença apenas no s1
s6 = s2 - s1 #diferença apenas no s2
print(s5)
print(s6)

s7 = s1 ^ s2 #diferença simétrica
print(s7)