"""
Escopo de funcoes em Python
Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o codigo é alcancavel
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcacados.
"""

x = 1
print(x)

def escopo():
    global x
    x = 10
    print(x)
    
    def outra_funcao():
        global x
        x = 11        
        y = 12
        print(x,y)
    outra_funcao()

escopo()
print(x)